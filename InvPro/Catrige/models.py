from django.db import models

#Цвета
class Color(models.Model):
    name = models.CharField('Цвет', max_length=10)
    imageColor = models.ImageField()

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural='Цвета'

        def __str__(self):
            return self.name
