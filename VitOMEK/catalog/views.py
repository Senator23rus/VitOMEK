from django.shortcuts import render
from .models import *
from django.views import generic
from .permissions import SalesmanPermissionsMixin

def index(request):

    return render(request, 'index.html')

class PremixListView(generic.ListView):
    model = ProductPremix


class ProductPremixDetalView(generic.DetailView):
    model = ProductPremix

# class SalesmanProductPremixDetalView(SalesmanPermissionsMixin, generic.DetailView):
#     model = ProductPremix
