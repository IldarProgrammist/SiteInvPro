# Generated by Django 3.0.7 on 2020-06-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Printer', '0005_auto_20200613_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrinterStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Название статуса')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
    ]