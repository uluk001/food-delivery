from apps.core.models import Category, Customer, FoodCard, Order, ProductsCart
from django.contrib import admin

admin.site.register(Category)
admin.site.register(FoodCard)
admin.site.register(ProductsCart)
admin.site.register(Order)
admin.site.register(Customer)
