from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path for the home page
    path('', views.index, name='index'),
    #path for the products
    path('products/', views.product_list, name='product_list'),
    #path for product details.
    path('<slug:slug>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)