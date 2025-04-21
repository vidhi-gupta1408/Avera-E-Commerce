from django.shortcuts import render
from .models import Item

def item_list(request):
    context = {
        'items': Item.objects.all() 
    }
    return render(request, "index.html", context)

def shop(request):
    return render(request, 'product.html')

# Features view
def features(request):
    return render(request, 'shopping-cart.html')

# Blog view
def blog(request):
    return render(request, 'blog.html')

# About view
def about(request):
    return render(request, 'about.html')

# Contact view
def contact(request):
    return render(request, 'contact.html')

def header_view(request):
    return render(request, 'header.html')

def footer_view(request):
    return render(request, 'footer.html')

def login_view(request):
    return render(request, 'login.html')  # adjust path if namespaced

def cart_view(request):
    return render(request, 'shopping-cart.html')