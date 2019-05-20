from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return HttpResponse("Hello welcome to my django website")


# Create your views here.

