# Generated by Django 4.0.3 on 2022-04-05 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='StockPriceInfo',
        ),
    ]
