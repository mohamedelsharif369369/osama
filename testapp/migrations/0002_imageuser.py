# Generated by Django 5.1.4 on 2024-12-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=None, verbose_name='الصوره')),
                ('date', models.DateField(verbose_name='بتاريخ')),
            ],
            options={
                'verbose_name': 'img',
                'verbose_name_plural': 'imgs',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
