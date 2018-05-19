from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    vals = {'insert_me':"You got dick from the backend!"}
    return render(request, 'testapp/index.html', context=vals)

def about(request):
    return HttpResponse("<h1>This page is under construction</h1></br><h3>Check back later in sometime.</h3>")