# Generated by Django 3.0.7 on 2020-06-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0011_auto_20200614_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Зона'),
        ),
    ]
