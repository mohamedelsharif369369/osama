# Generated by Django 5.1.4 on 2024-12-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_masrof'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name=' المنتج')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name=' سعر البيع')),
                ('buing', models.DecimalField(decimal_places=2, max_digits=6, verbose_name=' سعر الشراء')),
                ('quantity', models.IntegerField(verbose_name=' الكميه')),
            ],
            options={
                'verbose_name': 'البضائع',
                'verbose_name_plural': 'البضائع',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
