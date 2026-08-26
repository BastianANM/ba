from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v1(request):
    return HttpResponse("<h1>vista 1 de app2</h1>")
def v2(request):
    return HttpResponse("<h1>vista 2 de app2</h1>")