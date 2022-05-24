from django.shortcuts import render
from .models import *

def index(request):
    # num_materials = TypeOfMaterials.objects.all().count()
    # num_animals = Animal.objects.all().count()
    # num_goods = Goods.objects.all().count()


    return render(request, 'index.html')

def Premix(request):
    # materials = Premix.objects.all()
    return render(request, 'premixes.html')

def Sk1(request):
    return render(request, 'sk1.html')


