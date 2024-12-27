from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Test(models.Model):
    name = models.CharField(_("الاسم"), max_length=50)
    age = models.IntegerField(_("العمر"),blank=True, null=True)
    job = models.CharField(_("الوظيفه"), max_length=50,blank=True, null=True)
    class Meta:
        verbose_name = _("تحت التجربه")
        verbose_name_plural = _("تحت التجربه")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse("_detail", kwargs={"pk": self.pk})

class ImageUser(models.Model):
    img = models.ImageField(_("الصوره"), upload_to="img_photos", height_field=None, width_field=None, max_length=None)
    date = models.DateField(_("بتاريخ"), auto_now=False, auto_now_add=False)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'img'
        verbose_name_plural = 'imgs'