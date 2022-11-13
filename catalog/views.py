from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def store(request):
    context = {}
    return render (request, 'store/store.html', context)

def cart(request):
    context = {}
    return render (request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render (request, 'store/checkout.html', context)


class RTX3060(TemplateView):
    template_name= 'store/rtx3060.html'

class RTX3070(TemplateView):
    template_name= 'store/rtx3070.html'

class RTX3080(TemplateView):
    template_name= 'store/rtx3080.html'