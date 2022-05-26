from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('premix/', views.Premix, name='premix'),
    path('sk1/', views.Sk1, name='sk1'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
