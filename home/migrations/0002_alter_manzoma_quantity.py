# Generated by Django 5.1.4 on 2024-12-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manzoma',
            name='quantity',
            field=models.IntegerField(verbose_name=' الكميه'),
        ),
    ]
