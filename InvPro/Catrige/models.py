from django.db import models
from Printer.models import PrinterModel


# Цвета
class Color(models.Model):
    name = models.CharField('Цвет', max_length=10)
    imageColor = models.ImageField()

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

        def __str__(self):
            return self.name


# Добавление FirmCatrige

class FirmCatrige(models.Model):
    name = models.CharField('Фирма картриджа', max_length=20)

    class Meta:
        verbose_name = 'Фирма картриджа'
        verbose_name_plural = 'Фирмы картриджей'

        def __str__(self):
            return self.name


