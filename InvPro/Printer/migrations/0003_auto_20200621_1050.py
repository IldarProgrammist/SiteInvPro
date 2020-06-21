# Generated by Django 3.0.7 on 2020-06-21 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0002_printermodel_printercolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='modelPrinter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Printer.PrinterModel', verbose_name='Модель принтера'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='printermodel',
            name='printerColor',
            field=models.BooleanField(verbose_name='Является цветным'),
        ),
    ]
