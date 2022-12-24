from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def VBR(request):
    return HttpResponse('<h1><i><marquee>WORLD BEST BROTHER EVER</marquee></i></h1>')