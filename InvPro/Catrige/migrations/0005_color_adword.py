# Generated by Django 3.0.7 on 2020-06-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catrige', '0004_delete_firmcatrige'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='adword',
            field=models.CharField(default=1, max_length=1, verbose_name='Буква'),
            preserve_default=False,
        ),
    ]
