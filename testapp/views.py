from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Semester,Branch,Subject
# Create your views here.

def index(request):
    semval = Semester.objects.order_by('id')
    vals = {'SemHere' : semval}
    return render(request, 'testapp/index.html', context=vals)

def about(request):
    return HttpResponse("<h1>This page is under construction</h1></br><h3>Check back later in sometime.</h3>")