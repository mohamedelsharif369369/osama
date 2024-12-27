from django.contrib import admin
from .models import Hesabi
# Register your models here.


class HesabiAdmin(admin.ModelAdmin):
    list_display = ('price','day','at','month')
    list_filter = ('at','day','month','price')
    search_fields = ('at','day','month','price')
    ordering = ['at']
admin.site.register(Hesabi, HesabiAdmin)