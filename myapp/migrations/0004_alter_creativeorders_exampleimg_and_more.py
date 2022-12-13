# Generated by Django 4.1.1 on 2022-11-16 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_products_owncost_products_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativeorders',
            name='exampleImg',
            field=models.ImageField(blank=True, help_text='Чертеж или эскиз', null=True, upload_to='uploads/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='creativeorders',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 16, 11, 34, 24, 189798, tzinfo=datetime.timezone.utc), help_text='Дата заказа'),
        ),
    ]
