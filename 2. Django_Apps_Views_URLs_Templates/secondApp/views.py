from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home1(request):
    return HttpResponse('Hello World from App 2')

def home2(request):
    return HttpResponse("<b>This is Home 2 from App 2</b>")

def home3(request):
    return HttpResponse("<i>This is Home 3 from App 2</i>")