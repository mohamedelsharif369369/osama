
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Manzom(models.Model):
    code = models.IntegerField(_(" الكود"))
    quantity = models.IntegerField(_(" الكميه"))
    price = models.DecimalField(_(" الثمن"),max_digits=6,decimal_places=2)
    date = models.DateField(_(" التاريخ"), auto_now=False, auto_now_add=False,blank=True, null=True)
    img = models.ImageField(_("الصوره"), upload_to="pht")
    def __str__(self):
        return str(self.code)
    class Meta:
        db_table = ''
        managed = True
        verbose_name ='منظومة دعوات الافراح'
        verbose_name_plural = 'منظومة دعوات الافراح'
        ordering = ['price']