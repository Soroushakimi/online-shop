from django.contrib import admin
from django.urls import path
from .views import ProductShow,Details,cart_view,add_to_cart,remove_from_cart,remove_single_item_from_cart

urlpatterns = [
    
    path('productdetails/<int:id>', Details.as_view(),name='productdetails'),
    path('cart/', cart_view ,name='cart'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<int:id>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
]