from django.db import models


class PrinterFirm(models.Model):
    name = models.CharField('Фирма принтера', max_length=20)
    logo = models.ImageField()

    class Meta:
        verbose_name = 'Фирма принтера'
        verbose_name_plural = 'Фирмы принтеров'

    def __str__(self):
        return self.name


class PrinterModel(models.Model):
    name = models.CharField('Модель принтера', max_length=20)
    photo = models.ImageField()
    printerFirm = models.ForeignKey(PrinterFirm, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модели принтеров'

    def __str__(self):
        return self.name
    

