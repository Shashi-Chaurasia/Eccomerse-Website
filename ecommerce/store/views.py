from store.models import Product
from django.shortcuts import render
from .models import*


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request ,'store/store.html' ,context)

def cart(request):
    # Check authenticate user 
    # or user loged in
    if request.user.is_authenticated:
        #set cutomer values
        customer = request.user.customer # aceesc the customer one-one relation
        # order creater or order exist 
        order ,created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_item':0}


    context = {'items':items ,'order':order}
    return render(request ,'store/cart.html' ,context)

def checkout(request):
    if request.user.is_authenticated:
        #set cutomer values
        customer = request.user.customer # aceesc the customer one-one relation
        # order creater or order exist 
        order ,created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_item':0}

    context = {'items':items , 'order':order}
    return render(request ,'store/checkout.html' ,context)
