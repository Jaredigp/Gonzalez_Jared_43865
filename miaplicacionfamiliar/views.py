from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,"miaplicacionfamiliar/base.html")

def familia(request):
    return render(request,"miaplicacionfamiliar/familia.html")

def ascendencia(request):
    return render(request,"miaplicacionfamiliar/ascendencia.html")

def ocupacion(request):
    ocupacion_familiares = {"ocupacion" : Ocupacion.objects.all()}
    return render(request,"miaplicacionfamiliar/ocupacion.html",ocupacion_familiares)