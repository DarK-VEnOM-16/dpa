from django import urls
from django.urls import path,include
from . import views

urlpatterns = [
    path(r"",views.index,name="Home"),
    path(r"about",views.about,name="about"),
    path(r"service",views.services,name="services"),
    path(r"contact",views.contact,name="contact"),

    path(r'^(?P<album_id>[0-9]+$)/',views.details,name="details")
    
]