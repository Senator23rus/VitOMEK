from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materials/', views.MaterialsListView, name='materials'),
    path('blands/', views.BlandsListView, name='blands'),
    path('premix/', views.TypePremixListView, name='premix'),
    path('bvmk/', views.BvmkListView, name='bvmk'),
]
