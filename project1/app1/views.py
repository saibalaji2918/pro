from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return HttpResponse('<h1>data is sucussesfully updated</h1>')

