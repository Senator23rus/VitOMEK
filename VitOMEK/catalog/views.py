from django.shortcuts import render
from .models import *

def index(request):
    num_materials = Materials.objects.all().count()
    num_blands = Blands.objects.all().count()
    num_premix = TypeOfPremix.objects.all().count()
    num_BVMK = bvmk.objects.all().count()

    return render(request, 'index.html', context={'num_materials': num_materials,
                                                  'num_blands': num_blands,
                                                  'num_premix': num_premix,
                                                  'num_BVMK': num_BVMK,
                                                  })

def MaterialsListView(request):
    materials = Materials.objects.all()
    return render(request, 'materials_list.html', context={'materials': materials,})

def BlandsListView(request):
    blands = Blands.objects.all()
    return render(request, 'blands_list.html', context={'blands': blands,})

def TypePremixListView(request):
    premix = TypeOfPremix.objects.all()
    return render(request, 'premix_list.html', context={'premix': premix,})

def BvmkListView(request):
    bvmk = TypeOfPremix.objects.all()
    return render(request, 'bvmk_list.html', context={'bvmk': bvmk,})
