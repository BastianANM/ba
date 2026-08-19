from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1(request):
    return HttpResponse("<h1>Hola mundo desde la vista 1 de app1</h1>"
    "<p style='color:blue'> todo lo que necesitas </p>")
def vista2(request):
    return HttpResponse("<h1>Hola mundo desde la vista 2 de app1</h1>")