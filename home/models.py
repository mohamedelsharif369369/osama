from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Manzoma(models.Model):
    code = models.IntegerField(_(" الكود"))
    quantity = models.IntegerField(_(" الكميه"))
    price = models.DecimalField(_(" الثمن"),max_digits=6,decimal_places=2)
    date = models.DateField(_(" التاريخ"), auto_now=False, auto_now_add=False,blank=True, null=True)
    img = models.ImageField(_(" الصوره"),upload_to='photos', height_field=None, width_field=None,blank=True, null=True)
    def __str__(self):
        return str(self.code)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='منظومة دعوات الافراح'
        verbose_name_plural = 'منظومة دعوات الافراح'
        ordering = ['code']
    
class Hesabi(models.Model):
    price = models.DecimalField(_(" مصروف"),max_digits=5, decimal_places=2)
    day = models.CharField(_("يوم"), max_length=50)
    at = models.DateField(_(" الموافق"),auto_now=False, auto_now_add=False)
    month = models.CharField(_(" الشهر"),max_length=5,blank=True, null=True)
    def __str__(self):
        return str(self.at)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='حسابى'
        verbose_name_plural = 'حسابى'
        ordering = ['at']

class Masrof(models.Model):
    msrof = models.DecimalField(_(" مصروف"),max_digits=5, decimal_places=2)
    name = models.CharField(_(" لحساب"),max_length=50)
    day = models.CharField(_("يوم"), max_length=50)
    date = models.DateField(_(" الموافق"),auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='مصاريف'
        verbose_name_plural = 'مصاريف'
        ordering = ['date']

class Product(models.Model):
    name = models.CharField(_(" المنتج"),max_length=90)
    price = models.DecimalField(_(" سعر البيع"),max_digits=6, decimal_places=2)
    buing = models.DecimalField(_(" سعر الشراء"),max_digits=6, decimal_places=2,blank=True, null=True)
    quantity = models.IntegerField(_(" الكميه"))
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='البضائع'
        verbose_name_plural = 'البضائع'
        ordering = ['name']


class Servie(models.Model):
    name = models.CharField(_(" العميل"),max_length=99)
    servies = models.CharField(_(" الخدمه"),max_length=99)
    price = models.DecimalField(_(" سعرها"),max_digits=6, decimal_places=2)
    paid = models.DecimalField(_(" مدفوع"),max_digits=6, decimal_places=2)
    paid_at = models.DateField(_(" بتاريخ"),auto_now=False, auto_now_add=False)
    rest = models.DecimalField(_(" متبقى"),max_digits=6, decimal_places=2,blank=True, null=True)
    delivery_time = models.DateField(_(" التسليم فى"),auto_now=False, auto_now_add=False,blank=True, null=True)
    phone = models.IntegerField(_(" الهاتف"),blank=True, null=True)
    tslem = models.CharField(_("  الحاله"), max_length=50,blank=True, null=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='الخدمات'
        verbose_name_plural = 'الخدمات'
        ordering = ['paid_at']


class Yaomia(models.Model):
    day = models.CharField(_(" اليوم"),max_length=50)
    day_date = models.DateField(_(" الموافق"),auto_now=False, auto_now_add=False)
    servies = models.CharField(_(" الخدمه"),max_length=50)
    price = models.DecimalField(_(" ثمنها"),max_digits=5, decimal_places=2)
    rest = models.DecimalField(_(" متبقى"),max_digits=5, decimal_places=2,blank=True, null=True)
    phone = models.IntegerField(_(" الهاتف"),blank=True, null=True)
    def __str__(self):
        return str(self.day)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='دفتر اليوميه'
        verbose_name_plural = 'دفتر اليوميه'
        ordering = ['day_date']

