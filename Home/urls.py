from django import urls
from django.urls import path,include
from . import views

urlpatterns = [
    path(r"",views.index,name="Home"),
    path(r"europe/",views.europe,name="about"),
    path(r"asia/",views.asia,name="about"),
    path(r"australia/",views.australia,name="about"),
    path(r"southamerica/",views.southamerica,name="about"),
    path(r"northamerica/",views.northamerica,name="services"),
    path(r"contact",views.contact,name="contact"),

    path(r'^(?P<album_id>[0-9]+$)/',views.details,name="details")
    
]