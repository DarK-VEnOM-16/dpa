from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import data

def index(request):
    content={
        'cont'  : 'all',
        'data'  : data.objects.all()
    }
    return render(request,'index1.html',content)

def europe(request):
    content={
        'cont'  : "eu",
        'data'  : data.objects.filter(continent="United Kingdom")
    }
    return render(request,'index1.html',content)    
def australia(request):
    content={
        'cont'  : "aus",
        'data'  : data.objects.filter(continent="Australia")
    }
    return render(request,'index1.html',content)    
def asia(request):
    content={
        'cont'  : "as",
        'data'  : data.objects.filter(continent="Asia")
    }
    return render(request,'index1.html',content)    
def northamerica(request):
    content={
        'cont'  : "na",
        'data'  : data.objects.filter(continent="northamerica")
    }
    return render(request,'index1.html',content)    
def southamerica(request):
    content={
        'cont'  : "sa",
        'data'  : data.objects.filter(continent="southamerica")
    }
    return render(request,'index1.html',content)    



def services(request):
    return HttpResponse("<h1>Hello~~~World</h1><h1>How are you</h1><h1>This is Service page</h1>")

def contact(request):
    return HttpResponse("<h1>Hello~~~World</h1><h1>How are you</h1><h1>This is Contact page</h1>")

def details(request,album_id):
    return HttpResponse("<h2>DEtails for AlbumId : "+str(album_id)+"</h2>")
