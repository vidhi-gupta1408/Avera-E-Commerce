from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User #Import User model


class HomeView(ListView):
    model = Item
    template_name = "index.html"

class ShopView(ListView):
    model = Item
    template_name = "product.html"

class ProductDetail(DetailView):
    model = Item
    template_name = "product-detail.html"

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def header_view(request):
    return render(request, 'header.html')

def footer_view(request):
    return render(request, 'footer.html')

def login_view(request):
    return render(request, 'login.html')

def cart_default_view(request):
    return render(request, 'shopping-cart.html')

# Add this new view
def product_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'product-detail.html', {'object': item})

# Secure cart_view to POST only
@require_POST
def cart_view(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # Use get_or_create to handle order creation/retrieval
    order, created = Order.objects.get_or_create(user=request.user, ordered=False)

    order_item_qs = order.items.filter(item=item)  # Changed item__slug to item

    if order_item_qs.exists():
        order_item = order_item_qs.first()
        order_item.quantity += 1
        order_item.save()
        print(
            f"Increased quantity of {item.title} to {order_item.quantity}")  # Debugging
    else:
        order_item = OrderItem.objects.create(item=item, quantity=1)  # set quantity here
        order.items.add(order_item)
        print(f"Added {item.title} to order")  # Debugging

    order.ordered_date = timezone.now()  # set ordered_date
    order.save()  # save order
    print(
        f"Order ID: {order.id}, User: {request.user.username}, Ordered: {order.ordered}")  # Debugging
    return redirect('core:cart')
