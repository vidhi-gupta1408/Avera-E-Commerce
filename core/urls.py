from django.urls import path
# from .views import item_list
from . import views
from .views import item_list, header_view  # make sure header_view is imported!
app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('shop/', views.shop, name='shop'),  # URL for Shop
    path('features/', views.features, name='features'),  # URL for Features
    path('blog/', views.blog, name='blog'),  # URL for Blog
    path('about/', views.about, name='about'),  # URL for About
    path('contact/', views.contact, name='contact'),  # URL for Contact
    path('header/', views.header_view, name='header'),  # ← ADD THIS
    path('footer/', views.footer_view, name='footer'),
    path('login/', views.login_view, name='login'),

]