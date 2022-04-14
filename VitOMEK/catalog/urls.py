from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materials/', views.TypeOfMaterialsListView, name='materials'),
    path('goods/', views.GoodsListView, name='goods'),
    path('animals/', views.AnimalListView, name='animals'),

]
