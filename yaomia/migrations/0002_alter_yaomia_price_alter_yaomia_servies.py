# Generated by Django 5.1.4 on 2024-12-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaomia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yaomia',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' ثمنها'),
        ),
        migrations.AlterField(
            model_name='yaomia',
            name='servies',
            field=models.CharField(max_length=50, verbose_name=' الخدمه'),
        ),
    ]