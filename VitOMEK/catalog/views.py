from django.shortcuts import render
from .models import *

def index(request):

    return render(request, 'index.html')

def Premix(request):
    return render(request, 'premixes.html')

def Sk1(request):
    return render(request, 'sk1.html')


