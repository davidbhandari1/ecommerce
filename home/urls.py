
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('my-account', my_account, name='my-account'),
    path('product-detail', product_detail, name='product-detail'),
    path('product-list', product_list, name='product-list'),
    path('base', base, name='base'),
    path('wishlist', wishlist, name='wishlist'),

]
