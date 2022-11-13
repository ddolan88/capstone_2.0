from django.urls import path
from . import views

urlpatterns = [
    # path('', views.store, name='store'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='update_order')
]
from django.urls import path
from . import views
from .views import (
    RTX3060,
    RTX3070,
    RTX3080,
)
urlpatterns = [
    path('store/', views.store, name='store'),
    # path('cart/', views.cart, name = 'cart'),
    # path('checkout/', views.checkout, name = 'checkout'),
    path('rtx3060/', RTX3060.as_view(), name = 'rtx3060'),
    path('rtx3060/', RTX3070.as_view(), name = 'rtx3070'),
    path('rtx3060/', RTX3080.as_view(), name = 'rtx3080'),
]
