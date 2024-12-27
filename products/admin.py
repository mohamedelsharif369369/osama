from django.contrib import admin

from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','buing','quantity')
    list_filter = ('quantity','name')
    search_fields = ('quantity','name')
    ordering = ['name']
admin.site.register(Product, ProductAdmin)
