from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    """Home page view."""
    featured_products = Product.objects.filter(is_active=True)[:6]
    context = {'featured_products': featured_products}
    return render(request, 'products/index.html', context)


def product_list(request):
    """View function for the list of products."""
    products = Product.objects.filter(is_active=True)
    context = {'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    """View function for the deatils about ab specific product."""
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
