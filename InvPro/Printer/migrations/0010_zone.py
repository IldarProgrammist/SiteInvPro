# Generated by Django 3.0.7 on 2020-06-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0009_auto_20200614_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Зона')),
            ],
            options={
                'verbose_name': 'Зона',
                'verbose_name_plural': 'Зоны',
            },
        ),
    ]