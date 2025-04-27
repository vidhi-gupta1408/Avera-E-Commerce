from django.contrib import admin
from .models import Item, OrderItem, Order

class OrderItemInline(admin.TabularInline):
    model = Order.items.through  # Use the through model
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['user', 'ordered_date', 'ordered', 'get_items']  # Add get_items
    list_filter = ['user', 'ordered']  # Add list_filter
    
    def get_items(self, obj):
        return ", ".join([str(item) for item in obj.items.all()])
    get_items.short_description = 'Items'

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']
    list_filter = ['item'] # Added filter to OrderItemAdmin

admin.site.register(Item)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)