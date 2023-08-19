from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home1(request):
    # request arg will contain the payload of request sent to a URL, 
    return HttpResponse('Hello World')
    # return of a django view is either Template, HTML String, String,
    # JSON (when working as API)

def home2(request):
    return HttpResponse("<b>This is Home 2</b>")

def home3(request):
    return redirect('/secondApp/1')
    return HttpResponse("<i>This is Home 3</i>")

def home4(request):
    return redirect('secondApp:home1')

def home5(request):
    my_dict = {'Name': 'Ali', 'Age': 22}
    return JsonResponse(my_dict)