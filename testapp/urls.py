from django.urls import path
from . import views

#Template Tagging
app_name = 'testapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('formpg/',views.formpg,name = 'Someform')
]