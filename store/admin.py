from django.contrib import admin
from store.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Add_to_cart)
admin.site.register(wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)