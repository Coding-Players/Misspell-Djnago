from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, ListView, CreateView, TemplateView
# from ShopHome.ShopHomeForm import MedicineForm
from ShopHome.models import Products, Order, OrderedItem
from Account.models import ServiceProviderProfile


def ShopHome(requests):
    """
    This is the home page when we open the browser this section show fast
    """
    return render(requests, "ShopHome/Home/home.html")


def all_products(requests):
    products = Products.objects.all()
    context = {'products': products}
    return render(requests, "ShopHome/Products/All_Products.html", context)


def cart_page(requests):
    if requests.user.is_authenticated:
        customer = requests.user.normalprofile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.ordereditem_set.all()
        print(created)
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {'items': items, 'order': order}
    return render(requests, "ShopHome/ShopingCart/Shopin_Cart.html", context)


@login_required(login_url='LogIn')
def products_upload(requests, pk):
    service_provider_profile_data = ServiceProviderProfile.objects.filter(user=requests.user)
    for service_provider_data in service_provider_profile_data:
        if service_provider_data.SerV_address == "" and service_provider_data.SerV_phone_no == "":
            # print(service_provider_data.SerV_name)
            # print(service_provider_data.SerV_birth_date)
            # print(service_provider_data.SerV_age)
            # print(service_provider_data.SerV_address)
            # print(service_provider_data.SerV_phone_no)
            # print(service_provider_data.SerV_gender)
            messages.info(requests, f"{service_provider_data.SerV_name} Please Create Service Provider Account First.")
            return redirect(f"/Account/ServiceProvider_Profile_Update/{pk}/")
    return render(requests, 'ShopHome/Products/UploadProducts.html')

