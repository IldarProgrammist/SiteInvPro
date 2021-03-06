# Generated by Django 3.0.7 on 2020-06-26 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catrige', '0017_delete_extradition'),
    ]

    operations = [
        migrations.CreateModel(
            name='JurnalCatrige',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateExtation', models.DateField(auto_now=True)),
                ('serialNumberCatrige', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catrige.Catrige', verbose_name='Серийный номер')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catrige.StatusCatrige', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус картриджа',
                'verbose_name_plural': 'Статусы картриджей',
            },
        ),
    ]
