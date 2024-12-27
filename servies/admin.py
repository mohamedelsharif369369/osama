from django.contrib import admin

from .models import Servie
# Register your models here.
class ServieAdmin(admin.ModelAdmin):
    list_display = ('name','servies','price','paid','paid_at','rest','delivery_time','phone','tslem')
    list_filter = ('servies','name','price','paid_at','delivery_time','tslem')
    search_fields = ('servies','name','price','paid_at','delivery_time','tslem')
    ordering = ['paid_at']
admin.site.register(Servie, ServieAdmin)
