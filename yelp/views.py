from django.shortcuts import render
from yelp.models import Cuisine
from django.http import HttpResponse
from yelp.forms import CuisineForm
from django_yelp import credentials

import requests
import json

AUTH_HEADER = {"Authorization":"Bearer {}".format(credentials.YELP_API_KEY)}

# Create your views here.
def index(request):
    if request.method == 'GET' and not request.GET.get('cuisine', ''):
        form = CuisineForm()
        return render(request, 'yelp/yelp.html', {'form': form})
    else:
        query = request.GET.get('cuisine', '')
        form = CuisineForm(initial={'cuisine': query})
        r = requests.get('https://api.yelp.com/v3/businesses/search', headers=AUTH_HEADER, params={'term': query,
                                                                                                    'categories': 'restaurants',
                                                                                                    'latitude': '37.786882',
                                                                                                    'longitude': '-122.399972'})
        businesses = []
        error = False
        if r.status_code == 200:
            api_data = r.json()
            if api_data['businesses']:
                businesses_unfiltered = api_data['businesses'][10:]
                for business in businesses_unfiltered:
                    temp = {}
                    temp['image_url'] = business.get('image_url', '')
                    temp['name'] = business.get('name', 'N/A')
                    temp['location'] = ' '.join(business['location'].get('display_address', 'N/A'))
                    temp['phone'] = business.get('display_phone', 'N/A')
                    temp['price'] = business.get('price', 'N/A')
                    temp['rating'] = business.get('rating', 'N/A')
                    businesses.append(temp)
                    del temp
            return render(request, 'yelp/yelp.html', {'form': form, 'query': query, 'businesses': businesses})
        else:
            error = True
            return render(request, 'yelp/yelp.html', {'form': form, 'error': error})



def get_cuisine_autocomplete(request):
    if request.is_ajax():
        term = request.GET.get('term', '')
        cuisines = Cuisine.objects.filter(name__contains=term)[:20]
        results = []
        for cuisine in cuisines:
            cuisine_json = {}
            cuisine_json['id'] = cuisine.id
            cuisine_json['label'] = cuisine.name
            cuisine_json['value'] = cuisine.name
            results.append(cuisine_json)
        data = json.dumps(results)
    else:
        data = 'ERROR'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
