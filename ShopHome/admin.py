from django.contrib import admin
from ShopHome.models import Products, Order,\
    OrderedItem
    # GreenVegetable, Grocery, Medicine


# admin.site.register(GreenVegetable)
# admin.site.register(Grocery)
# admin.site.register(Medicine)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderedItem)

