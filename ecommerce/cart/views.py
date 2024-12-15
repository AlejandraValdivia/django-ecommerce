from django.shortcuts import render

from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, 'cart/cart-summary.html')
    pass

def cart_add(request):

    cart = Cart(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_qty)
    # return render(request, 'cart/add.html')
    pass

def cart_delete(request):
    # return render(request, 'cart/delete.html')
    pass

def cart_update(request):
    # return render(request, 'cart/update.html')
    pass