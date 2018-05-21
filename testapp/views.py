from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Semester,Branch,Subject
from . import forms
# Create your views here.

def index(request):
    semval = Semester.objects.order_by('id')
    vals = {'SemHere' : semval}
    return render(request, 'testapp/index.html', context=vals)

def about(request):
    return HttpResponse("<h1>This page is under construction</h1></br><h3>Check back later in sometime.</h3>")

def formpg(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print("Name: "+form.cleaned_data['name'])
            print("Name: "+form.cleaned_data['email'])
            print("Name: "+form.cleaned_data['text'])
                        
    return render(request,'testapp/forms.html',{'form':form})