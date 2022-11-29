from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
import json
from .models import *
import datetime
from catalog.models import Customer


# context = {'items': items, 'order': order}

# Create your views here.


def store(request):

    if request.user.is_authenticated:
        customer= Customer.objects.filter(user=request.user).first()
        # customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        cartItems = order.orderitem_set.all()
        # cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = []

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        # customer = request.user.customer
        customer= Customer.objects.filter(user=request.user).first()
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        cartItems = order.orderitem_set.all()
        # cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    customer = request.user.cusomer
    product = product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (order.Item.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (order.Item.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
    else:
        print("user not logged in")
    return JsonResponse('Order was complete')




# Create your views here.


class RTX3060(TemplateView):
    template_name= 'store/rtx3060.html'

class RTX3070(TemplateView):
    template_name= 'store/rtx3070.html'
    

class RTX3080(TemplateView):
    template_name= 'store/rtx3080.html'