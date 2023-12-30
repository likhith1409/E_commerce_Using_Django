# myapp/admin.py
from django.contrib import admin
from .models import Customer, Product, Order

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    search_fields = ['name', 'email']
    ordering = ['id']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']
    ordering = ['id']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)



