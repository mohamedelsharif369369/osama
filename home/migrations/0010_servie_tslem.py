# Generated by Django 5.1.4 on 2024-12-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_manzoma_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='servie',
            name='tslem',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='  الحاله'),
        ),
    ]
