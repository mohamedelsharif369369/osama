# Generated by Django 5.1.4 on 2024-12-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_servie_tslem'),
    ]

    operations = [
        migrations.AddField(
            model_name='hesabi',
            name='day',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='يوم'),
        ),
        migrations.AddField(
            model_name='masrof',
            name='day',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='يوم'),
        ),
        migrations.AlterField(
            model_name='hesabi',
            name='at',
            field=models.DateField(verbose_name=' الموافق'),
        ),
        migrations.AlterField(
            model_name='masrof',
            name='date',
            field=models.DateField(verbose_name=' الموافق'),
        ),
    ]
