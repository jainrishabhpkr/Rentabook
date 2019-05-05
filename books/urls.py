from django.conf.urls import url
from django.contrib import admin
from books import views

urlpatterns = [

    url(r'^index/', views.indexview, name ='books'),
    url(r'^(?P<book_id>\d+)/', views.bookview, name= 'book'),
    url(r'^search/', views.searchview, name= 'search'),

]
