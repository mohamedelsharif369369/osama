from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Masrof(models.Model):
    msrof = models.DecimalField(_(" مصروف"),max_digits=5, decimal_places=2)
    name = models.CharField(_(" لحساب"),max_length=50)
    day = models.CharField(_("يوم"), max_length=50)
    date = models.DateField(_(" الموافق"),auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.msrof)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='مصاريف'
        verbose_name_plural = 'مصاريف'
        ordering = ['date']

