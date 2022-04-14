from django.shortcuts import render
from .models import *

def index(request):
    num_materials = TypeOfMaterials.objects.all().count()
    num_animals = Animal.objects.all().count()
    num_goods = Goods.objects.all().count()


    return render(request, 'index.html', context={'num_materials': num_materials,
                                                  'num_animals': num_animals,
                                                  'num_goods': num_goods,
                                                  })

def TypeOfMaterialsListView(request):
    materials = TypeOfMaterials.objects.all()
    return render(request, 'materials_list.html', context={'materials': materials,})

def GoodsListView(request):
    goods = Goods.objects.all()
    return render(request, 'goods_list.html', context={'goods': goods,})

def AnimalListView(request):
    animal = Animal.objects.all()
    return render(request, 'animal_list.html', context={'animal': animal,})


