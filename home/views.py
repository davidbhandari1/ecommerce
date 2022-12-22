from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')


def base(request):
    return render(request,'base.html')

def cart(request):
    return render(request,'cart.html')

def wishlist(request):
    return render(request,'wishlist.html')

def checkout(request):
    return render(request,'checkout.html')


def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def my_account(request):
    return render(request,'my-account.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def product_list(request):
    return render(request,'product-list.html')

