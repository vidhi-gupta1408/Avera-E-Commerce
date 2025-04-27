from django.urls import path
from . import views
from .views import (    
    header_view,
    HomeView,
    ShopView,
    ProductDetail
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
    path('shopping-cart/', views.cart_default_view, name='cart'),
    path('shopping-cart/<slug>/', views.cart_view, name='cart-default'),
    path('product/<slug>/', views.product_detail, name='product-detail'),  # Add this line
]
