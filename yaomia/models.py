from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Yaomia(models.Model):
    day = models.CharField(_(" اليوم"),max_length=50)
    day_date = models.DateField(_(" الموافق"),auto_now=False, auto_now_add=False)
    servies = models.CharField(_(" الخدمه"),max_length=50)
    price = models.DecimalField(_(" ثمنها"),max_digits=5, decimal_places=2)
    rest = models.DecimalField(_(" متبقى"),max_digits=5, decimal_places=2,blank=True, null=True)
    phone = models.IntegerField(_(" الهاتف"),blank=True, null=True)
    def __str__(self):
        return str(self.servies)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='دفتر اليوميه'
        verbose_name_plural = 'دفتر اليوميه'

