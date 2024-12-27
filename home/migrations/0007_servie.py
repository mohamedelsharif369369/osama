# Generated by Django 5.1.4 on 2024-12-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, verbose_name=' العميل')),
                ('servies', models.CharField(max_length=99, verbose_name=' الخدمه')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name=' سعرها')),
                ('paid', models.DecimalField(decimal_places=2, max_digits=6, verbose_name=' مدفوع')),
                ('paid_at', models.DateField(verbose_name=' بتاريخ')),
                ('rest', models.DecimalField(decimal_places=2, max_digits=6, verbose_name=' متبقى')),
                ('delivery_time', models.DateField(verbose_name=' التسليم فى')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name=' الهاتف')),
            ],
            options={
                'verbose_name': 'الخدمات',
                'verbose_name_plural': 'الخدمات',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
