from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/cuisine_autocomplete/', views.get_cuisine_autocomplete, name='cuisine_autocomplete'),
]