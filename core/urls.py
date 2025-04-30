from django.urls import path
from . import views
from .views import (    
    header_view,
    HomeView,
    ShopView,
    ProductDetail,
    cart_default_view,
    remove_cart_view,
    OrderSummaryView,
    remove_single_item_cart_view
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('features/<slug>/', ProductDetail.as_view(), name='features'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blog, name='blog-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('header/', views.header_view, name='header'),
    path('footer/', views.footer_view, name='footer'),
    path('login/', views.login_view, name='login'),
    # path('shopping-cart/', OrderSummaryView.as_view(), name='cart'),
    path('shopping-cart/', cart_default_view.as_view(), name='cart'),

    path('shopping-cart/<slug>/', cart_default_view.as_view(), name='cart-default'),
    path('remove-cart/<slug>/', remove_cart_view, name='remove-cart'),
    path('remove-single-item-cart/<slug>/', remove_single_item_cart_view, name='remove-single-item-cart'),
    path('product/<slug>/', views.product_detail, name='product-detail'),  # Add this line
]
