from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Home(request):
    return HttpResponse("welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")

def contact(request):
    return HttpResponse("contact us page")

def services(request):
    return HttpResponse("services page")