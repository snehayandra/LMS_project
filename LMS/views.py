from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse('We changed our project to LMS,Lets pray to get success in this atleast!!!')