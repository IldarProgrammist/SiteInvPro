from django.db import models
from django.db.models import CASCADE


# Цвета
class Color(models.Model):
    name = models.CharField('Цвет', max_length=10)
    adword = models.CharField(verbose_name='Буква', max_length=1)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


# Модели картриджей
class CatrigeModel(models.Model):
    name = models.CharField(verbose_name='Название модели', max_length=20)
    color = models.ForeignKey(Color, on_delete=CASCADE, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Модель картриджа'
        verbose_name_plural = 'Модели картриджей'

    def __str__(self):
        return self.name


# Статус картриджа
class StatusCatrige(models.Model):
    name = models.CharField(verbose_name='Название статуса', max_length=15)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Catrige(models.Model):
    serialNumber = models.CharField(max_length=15, verbose_name='Серийный номер', unique=True)
    modelCatrige = models.ForeignKey(CatrigeModel, on_delete=CASCADE, verbose_name='Модель картриджа')

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

    def __str__(self):
        return self.serialNumber


class StarusC(models.Model):
    serialNumber = models.ForeignKey(Catrige, verbose_name='Серийный номер', on_delete=models.CASCADE)
    catrigeStatus = models.ForeignKey(StatusCatrige, verbose_name='Статус картриджа', on_delete=models.CASCADE)
    dateChange = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Статус картриджа'
        verbose_name_plural = 'Статусы картриджей'
