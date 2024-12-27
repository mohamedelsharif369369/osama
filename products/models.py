from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

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



