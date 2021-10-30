from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    #if slug is provided, we are rendered a product list, filtered by the slug.
    #if slug is none, we go to the "" urplattern w/ all products.
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'shop/product/list.html', {'category': category, 'products': products, 'categories': categories})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True) #slug only needed for SEO-friendly URL;
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})