from django.conf.urls import url
from django.contrib import admin
from pages import views

urlpatterns = [
    
    url(r'^index/', views.indexview, name ='index'),
    url(r'^about/', views.aboutview, name= 'about'),
    url(r'^contactus/', views.contactusview, name= 'contactus'),
    url(r'^howitworks/', views.howitworksview, name= 'howitworks'),
]
