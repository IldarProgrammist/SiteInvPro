# Generated by Django 3.0.7 on 2020-06-14 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0015_typeroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationPrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberRoom', models.CharField(max_length=10, verbose_name='Номер кабинета')),
                ('numberTutul', models.ImageField(upload_to='', verbose_name='Номер титула')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('typeRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Printer.TypeRoom')),
            ],
        ),
    ]