from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('AP', 'All Products'),
    ('W', 'Women'),
    ('M', 'Men'),
    ('B', 'Bag'),
    ('S', 'Shoes'),
    ('WT', 'Watches'),
)

# LABEL_CHOICES = (
#     ('P', 'primary'),
#     ('S', 'secondary'),
#     ('D', 'danger')
# )
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    # label = models.CharField(choices = LABEL_CHOICES, max_length = 1)
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:features", kwargs={"slug": self.slug})

    def get_cart_view_url(self):
        return reverse("core:cart-default", kwargs={"slug": self.slug})
    
    def get_remove_cart_view_url(self):
        return reverse("core:remove-cart", kwargs={"slug": self.slug})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True, blank=True) #make ordered_date nullable
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
