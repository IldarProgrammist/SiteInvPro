# Generated by Django 3.0.7 on 2020-06-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0021_printer'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateChange', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('discription', models.TextField(blank=True, verbose_name='Описание')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Printer.Printer', verbose_name='Принтер')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Printer.Status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус принтера',
                'verbose_name_plural': 'Статусы принтеров',
            },
        ),
    ]
