# Generated by Django 4.2 on 2023-04-06 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='inventory_date',
        ),
    ]
