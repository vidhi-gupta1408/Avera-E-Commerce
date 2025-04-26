from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order
from django.shortcuts import redirect

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

def cart_default_view(request):
    return render(request, 'shopping-cart.html')

def cart_view(request, slug):
    item = get_object_or_404(Item, slug = slug)
    order_item = OrderItem.objects.create(item = item)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()

    else:
        order = Order.objects.create(user = request.user)
        order.items.add(order_item)
    
    return redirect("core:features", kwargs = {
        "slug": slug
    })