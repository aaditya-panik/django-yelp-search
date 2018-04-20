from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='yelp_index'),
    path('api/cuisine_autocomplete/', views.get_cuisine_autocomplete, name='cuisine_autocomplete'),
]