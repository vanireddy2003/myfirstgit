from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vani(request):
    return HttpResponse('<h1><marquee>EVERYTHING HAPPENS FOR A REASON</marquee></h1>')