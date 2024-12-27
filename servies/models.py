from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

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
        return str(self.servies)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='الخدمات'
        verbose_name_plural = 'الخدمات'
        ordering = ['paid_at']

