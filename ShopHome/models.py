from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from Account.models import NormalProfile, ServiceProviderProfile, DistributorProfile


class Products(models.Model):
    prod_upload_by = models.ForeignKey(to=ServiceProviderProfile, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=255)
    prod_picture = models.ImageField(upload_to='products/images')
    prod_price = models.FloatField(default=0, validators=[MinValueValidator(0)], max_length=20)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    in_terms_of = models.CharField(max_length=10,
                                   default="Male",
                                   choices=(
                                       ("pack", "pack"),
                                       ("piece", "piece"),
                                       ("kg", "kg"),
                                       ("gm", "gm"),
                                       ("L", "L"),
                                       ("ml", "ml"),
                                       ))
    prod_description = models.TextField()
    prod_offer = models.IntegerField(default=0,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)],
                                     null=True, blank=True
                                     )
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.prod_name

#
# class GreenVegetable(Products):
#     prod_upload_by = models.ForeignKey(to=ServiceProviderProfile, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
#     in_terms_of = models.IntegerField(choices=((1, '/kg'), (2, '/piece')), default=1)
#
#     def __str__(self):
#         return '%s' % self.prod_upload_by
#
#
# class Grocery(Products):
#     prod_upload_by = models.ForeignKey(to=ServiceProviderProfile, on_delete=models.CASCADE)
#     mfg_date = models.DateField(blank=False, null=True)
#     exp_date = models.DateField(blank=False, null=True)
#     quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
#     in_terms_of = models.IntegerField(choices=(
#         (1, '/kg'),
#         (2, '/gm'),
#         (3, '/L'),
#         (4, '/piece'),
#         (5, '/pack')
#     ), default=5)
#
#     def __str__(self):
#         return '%s' % self.prod_upload_by
#
#
# class Medicine(Products):
#     prod_upload_by = models.ForeignKey(to=ServiceProviderProfile, on_delete=models.CASCADE)
#     mfg_date = models.DateField(blank=False, null=True)
#     exp_date = models.DateField(blank=False, null=True)
#     quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
#     in_terms_of = models.IntegerField(choices=(
#         (1, '/pack'),
#         (2, '/piece'),
#         (3, '/L'),
#         (4, '/ml'),
#     ), default=1)
#
#     def __str__(self):
#         return '%s' % self.prod_upload_by


class Order(models.Model):
    customer = models.ForeignKey(to=NormalProfile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_item = self.ordereditem_set.all()
        total = sum([item.get_total for item in order_item])
        return total

    @property
    def get_cart_item(self):
        order_item = self.ordereditem_set.all()
        total = sum([item.quantity for item in order_item])
        return total


class OrderedItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    in_terms_of = models.IntegerField(choices=(
        (1, '/pack'),
        (2, '/piece'),
        (3, '/kg'),
        (4, '/gm'),
        (5, '/L'),
        (6, '/ml'),
    ), default=2)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.prod_price * self.quantity
        return total

