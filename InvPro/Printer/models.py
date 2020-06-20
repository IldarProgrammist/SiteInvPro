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


# Типа помещений

class TypeRoom(models.Model):
    name = models.CharField('Тип помещения', max_length=10)

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений'

    def __str__(self):
        return self.name


# Принтеры

class Printer(models.Model):
    serialNamber = models.CharField(verbose_name='Серийный номер', max_length=20)
    ip = models.CharField(verbose_name='ip-адрес', max_length=15)

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return format(self.serialNamber)


# Место расположения
class LocationPrinter(models.Model):
    serialNamber = models.ForeignKey(Printer, models.CASCADE, verbose_name='Серийный номер')
    numberRoom = models.CharField(verbose_name='Номер кабинета', max_length=10)
    typeRoom = models.ForeignKey(TypeRoom, on_delete=models.CASCADE, verbose_name='Тип помещения')
    numberTutul = models.IntegerField(verbose_name='Номер титула')
    floor = models.IntegerField(verbose_name='Этаж')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name='Зона')
    dateChange = models.DateTimeField(verbose_name='Дата', auto_now=True)

    class Meta:
        verbose_name = 'Место расположение'
        verbose_name_plural = 'Места расположания'

    def __str__(self):
        return 'Кабинет номер: {}'.format(self.numberRoom)


# Статус
class Status(models.Model):
    name = models.CharField(verbose_name='Статус', max_length=15)

    class Meta:
        verbose_name = 'Cтатус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


# Статус принтера

class StatusP(models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Серийный номер')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    dateChangeStatus = models.DateTimeField(verbose_name='Дата', auto_now=True)
    discription = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Статус принтера'
        verbose_name_plural = 'Статусы принтеров'
