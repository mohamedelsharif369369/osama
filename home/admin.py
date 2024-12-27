from django.contrib import admin
from .models import Manzoma, Hesabi, Masrof ,Product, Servie, Yaomia


# Register your models here.

#class ManzomaAdmin(admin.ModelAdmin):
    #list_display = ('code','price','quantity','date','img')
    #list_filter = ('code','price')
    #search_fields = ('code','price')
    #ordering = ['price']
#admin.site.register(Manzoma, ManzomaAdmin)


#class HesabiAdmin(admin.ModelAdmin):
    #list_display = ('price','day','at','month')
    #list_filter = ('at','month','day')
    #search_fields = ('at','month','day')
    #ordering = ['at','month','day']
#admin.site.register(Hesabi, HesabiAdmin)


#class MasrofAdmin(admin.ModelAdmin):
    #list_display = ('msrof','name','day','date')
    #list_filter = ('name','day','date')
    #search_fields = ('name','day','date')
    #ordering = ['date']
#admin.site.register(Masrof, MasrofAdmin)

#class ProductAdmin(admin.ModelAdmin):
 #   list_display = ('name','price','buing','quantity')
  #  list_filter = ('name',)
   # search_fields = ('name',)
    #ordering = ['price']
#admin.site.register(Product, ProductAdmin)

#class ServieAdmin(admin.ModelAdmin):
 #   list_display = ('name','servies','price','paid','paid_at','rest','delivery_time','phone','tslem')
  #  list_filter = ('name',)
   # search_fields = ('name',)
    #ordering = ['paid_at']
#admin.site.register(Servie, ServieAdmin)


#class YaomiaAdmin(admin.ModelAdmin):
 #   list_display = ('day','day_date','servies','price')
  #  list_filter = ('day','day_date','servies')
   # search_fields = ('day','day_date','servies')
    #ordering = ['day_date']
#admin.site.register(Yaomia, YaomiaAdmin)