from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import data
def index(request):
    content={
        'length':len(data.objects.all()),
        'data'  : data.objects.all()
    }
    return render(request,'index1.html',content)

def about(request):
    return HttpResponse("<h1>Hello~~~World</h1><h1>How are you</h1><h1>This is about page</h1>")

def services(request):
    return HttpResponse("<h1>Hello~~~World</h1><h1>How are you</h1><h1>This is Service page</h1>")

def contact(request):
    return HttpResponse("<h1>Hello~~~World</h1><h1>How are you</h1><h1>This is Contact page</h1>")

def details(request,album_id):
    return HttpResponse("<h2>DEtails for AlbumId : "+str(album_id)+"</h2>")
