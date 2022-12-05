from django.shortcuts import render, get_object_or_404
from .models import Type, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def prod_list(request, type_id=None):
    type = None
    products = Product.objects.filter(available=True)
    if type_id:
        type = get_object_or_404(Type, id=type_id)
        products = Product.objects.filter(type=type, available=True)

        paginator = Paginator(products, 6)
        try:
            page = int(request.GET.get('page', '1'))
        except: 
            page = 1
        try:
            products = paginator.page(page)
        except (EmptyPage,InvalidPage):
            products = paginator.page(paginator.num_pages)

    return render(request, 'shop/type.html', {'type':type, 'prods':products})

def product_detail(request, type_id, product_id):
    product = get_object_or_404(Product, type_id=type_id, id=product_id)
    return render(request, 'shop/product.html', {'product':product})
