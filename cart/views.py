from django.shortcuts import render

# Create your views here.
from cart import cart

def show_cart(request, template_name="cart/cart.html"):
    cart_item_count = cart.cart_item_count(request)
    return render(request,template_name,{'cart_item_count':cart_item_count,'page_title':'Shopping Cart'})
