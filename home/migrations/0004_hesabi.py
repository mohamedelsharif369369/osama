# Generated by Django 5.1.4 on 2024-12-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_manzoma_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hesabi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' مصروف')),
                ('at', models.DateField(verbose_name=' بتاريخ')),
                ('month', models.CharField(max_length=51, verbose_name=' الشهر')),
            ],
            options={
                'verbose_name': 'حسابى',
                'verbose_name_plural': 'حسابى',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
