# Generated by Django 3.0.7 on 2020-06-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catrige', '0013_catrige_original'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catrige',
            name='Original',
        ),
        migrations.AddField(
            model_name='catrige',
            name='original',
            field=models.BooleanField(default=1, verbose_name='Оригинал'),
            preserve_default=False,
        ),
    ]
