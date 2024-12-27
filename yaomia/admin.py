from django.contrib import admin

from .models import Yaomia
# Register your models here.
class YaomiaAdmin(admin.ModelAdmin):
    list_display = ('day','day_date','servies','price','rest','phone')
    list_filter = ('day','day_date','servies','price')
    search_fields = ('day','day_date','servies','price')
    ordering = ['day_date']
admin.site.register(Yaomia, YaomiaAdmin)
