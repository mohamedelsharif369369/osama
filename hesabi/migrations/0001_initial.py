# Generated by Django 5.1.4 on 2024-12-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hesabi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name=' مصروف')),
                ('day', models.CharField(blank=True, max_length=50, null=True, verbose_name='يوم')),
                ('at', models.DateField(verbose_name=' الموافق')),
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