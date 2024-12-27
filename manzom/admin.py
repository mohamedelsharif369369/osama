from django.contrib import admin
from .models import Manzom
# Register your models here.

class ManzomAdmin(admin.ModelAdmin):
    list_display = ('code','price','quantity','date','img')
    list_filter = ('code','price')
    search_fields = ('code','price')
    ordering = ['price']
admin.site.register(Manzom, ManzomAdmin)

