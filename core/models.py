from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse

class Item(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    discount_price = models.FloatField(blank = True, null = True)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:features", kwargs={"slug": self.slug})
    
    def get_cart_view_url(self):
        return reverse("core:cart", kwargs={"slug": self.slug})
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username