from django.contrib import admin
from core.models import Category, Customer, FoodCard, Order, ProductsCart

admin.site.register(Category)
admin.site.register(FoodCard)   
admin.site.register(ProductsCart)
admin.site.register(Order)
admin.site.register(Customer)

