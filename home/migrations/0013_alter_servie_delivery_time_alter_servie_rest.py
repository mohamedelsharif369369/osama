# Generated by Django 5.1.4 on 2024-12-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_hesabi_options_alter_manzoma_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servie',
            name='delivery_time',
            field=models.DateField(blank=True, null=True, verbose_name=' التسليم فى'),
        ),
        migrations.AlterField(
            model_name='servie',
            name='rest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name=' متبقى'),
        ),
    ]