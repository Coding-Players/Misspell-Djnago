from django.urls import path
from . import views
from ShopHome.views import *

urlpatterns = [
    path('', views.ShopHome, name='ShopHome'),
    path('All-products/', views.all_products, name='all_products'),
    path('products_upload/<int:pk>/', views.products_upload, name='products_upload'),

    # =========================[ Shoping Cart Page ]=======================
    path('Shoping_Cart/', views.cart_page, name='Shoping_Cart'),
]

