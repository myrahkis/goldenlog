# Generated by Django 4.1.1 on 2022-11-06 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='creativeorders',
            options={'verbose_name': 'CreativeOrder'},
        ),
        migrations.AlterModelOptions(
            name='creativeproducts',
            options={'verbose_name': 'CreativeProduct'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product'},
        ),
    ]
