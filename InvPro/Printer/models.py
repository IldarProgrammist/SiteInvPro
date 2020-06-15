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


class Zone(models.Model):
    name = models.CharField('Зона', max_length=100)

    class Meta:
        verbose_name = 'Зона'
        verbose_name_plural = 'Зоны'

    def __str__(self):
        return self.name


#Типа помещений

class TypeRoom(models.Model):
    name = models.CharField('Тип помещения', max_length=10)

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений'

    def __str__(self):
        return self.name


#Место расположения
class LocationPrinter(models.Model):
    numberRoom = models.CharField(verbose_name='Номер кабинета', max_length=10, unique=True)
    typeRoom = models.ForeignKey(TypeRoom, on_delete=models.CASCADE, verbose_name='Тип помещения')
    numberTutul = models.IntegerField(verbose_name='Номер титула')
    floor = models.IntegerField(verbose_name='Этаж')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name='Зона')

    class Meta:
        verbose_name = 'Место расположение'
        verbose_name_plural = 'Места расположания'

    def __str__(self):
        return 'Кабинет номер: {}'.format(self.numberRoom)


#Статус принтера
class Status(models.Model):
    name = models.CharField(verbose_name='Статус', max_length=15)

    class Meta:
        verbose_name = 'Cтатус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


    

