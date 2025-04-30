from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Item, OrderItem, Order
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import CheckoutForm

class HomeView(ListView):
    model = Item
    template_name = "index.html"

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user = self.request.user, ordered = False)
            context = {
                'object': order
            }
            return render(self.request, "shopping-cart.html", context)
        
        except ObjectDoesNotExist:
            messages.error(self.request, "No Active Order")
            return redirect("/")
                
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

class cart_default_view(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }

        return render(self.request, 'shopping-cart.html', context)
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('core:cart-default')


# Add this new view
def product_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'product-detail.html', {'object': item})

def cart_view(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item, 
        user=request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Cart Updated")
 
        else:
            messages.info(request, "Added to cart")
            order.items.add(order_item)  
            return redirect("core:cart")  

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user = request.user, ordered_date = ordered_date)
        order.items.add(order_item)
        messages.info(request, "Added to Cart")

    return redirect("core:features", slug = slug)

def remove_cart_view(request, slug):
    item = get_object_or_404(Item, slug=slug)

    order_qs = Order.objects.filter(user = request.user, ordered = False)
    
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(
                item = item, 
                user=request.user,
                ordered = False
            )[0]

            order.items.remove(order_item)
            messages.info(request, "Item Removed")

        else:
            messages.info(request, "Not in Cart")
            return redirect("core:cart")
    
    else:
        messages.info(request, "No active order")
        return redirect("core:features", slug = slug)
    
    return redirect("core:cart")

def remove_single_item_cart_view(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "Item quantity updated")
            else:
                order.items.remove(order_item)
                messages.info(request, "Item removed from cart")
        else:
            messages.info(request, "Item not in cart")
    else:
        messages.info(request, "No active order")

    return redirect("core:cart")


