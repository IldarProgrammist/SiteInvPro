# Generated by Django 3.0.7 on 2020-06-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0023_auto_20200620_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusp',
            old_name='dateChange',
            new_name='dateChangeStatus',
        ),
    ]
