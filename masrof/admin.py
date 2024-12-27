from django.contrib import admin
from .models import Masrof
# Register your models here.


class MasrofAdmin(admin.ModelAdmin):
    list_display = ('msrof','name','day','date')
    list_filter = ('msrof','day','name','date')
    search_fields = ('msrof','day','name','date')
    ordering = ['date']
admin.site.register(Masrof, MasrofAdmin)
