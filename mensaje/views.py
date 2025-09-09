from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
  return HttpResponse("Hola desde Django, soy Blanco Romero Juan, listo para PythonAnywhere!")

# Create your views here.
