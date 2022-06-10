from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('premix/', views.PremixListView.as_view(), name='premix-list'),
    path('<int:pk>/', views.ProductPremixDetalView.as_view(), name='product-detail'),
    # path('<int:pk>/', views.SalesmanProductPremixDetalView.as_view(), name='product-salesman'),
    path('accounts/', include('django.contrib.auth.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

