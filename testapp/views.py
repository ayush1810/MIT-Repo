from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World");

def about(request):
    return HttpResponse("<h1>This page is under construction</h1></br><h3>Check back later in sometime.</h3>")