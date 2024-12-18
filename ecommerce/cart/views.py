from django.shortcuts import render

from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart-summary.html', {'cart': cart})
    

def cart_add(request):

    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)
    # if product is not None and product_quantity > 0:
    #     cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response
    

def cart_delete(request):
    # return render(request, 'cart/delete.html')
    pass

def cart_update(request):
    # return render(request, 'cart/update.html')
    pass