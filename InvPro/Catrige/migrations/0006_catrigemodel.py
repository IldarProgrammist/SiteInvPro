# Generated by Django 3.0.7 on 2020-06-21 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catrige', '0005_color_adword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatrigeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название модели')),
                ('adword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catrige.Color', verbose_name='Цвет')),
            ],
        ),
    ]
