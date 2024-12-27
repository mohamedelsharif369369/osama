from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

    
class Hesabi(models.Model):
    price = models.DecimalField(_(" مصروف"),max_digits=5, decimal_places=2)
    day = models.CharField(_("يوم"), max_length=50)
    at = models.DateField(_(" الموافق"),auto_now=False, auto_now_add=False)
    month = models.CharField(_(" الشهر"),max_length=51,blank=True, null=True)
    def __str__(self):
        return str(self.price)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='حسابى'
        verbose_name_plural = 'حسابى'