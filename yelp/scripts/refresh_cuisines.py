from yelp.models import Cuisine
import requests

def run():
    cuisines = Cuisine.objects.all()
    if cuisines:
        cuisines.delete()

    supported_categories = requests.get('https://www.yelp.com/developers/documentation/v3/all_category_list/categories.json')
    supported_categories = supported_categories.json()
    category_list = list(filter(lambda x: x['parents'], supported_categories))
    cuisine_list = list(filter(lambda x: x['parents'][0]==u'restaurants', category_list))
    for cuisine in cuisine_list:
        c = Cuisine(label=cuisine['alias'], name=cuisine['title'])
        c.save()
