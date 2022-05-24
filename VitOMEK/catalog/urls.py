from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('premix/', views.Premix, name='premix'),
    path('sk1/', views.Sk1, name='sk1'),

]
