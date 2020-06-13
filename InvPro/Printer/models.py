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

class Location(models.Model):
    titul = models.CharField(verbose_name='Титул',max_length=10)    
    room = models.CharField(verbose_name='Кабинет', max_length=10)
    floor = models.IntegerField(verbose_name='Этаж')


    class Meta:
        verbose_name = 'Место расположения'
        verbose_name_plural = 'Места расположения'

        def __str__(self):
            return self.room, self.floor
            
            
class PrinterStatus(models.Model):
    name = models.CharField(verbose_name='Название статуса', max_length=10)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        
        def __str__(self):
            return self.name


class Printer(models.Model):
    serialNumber = models.CharField(verbose_name='Серийный номер', max_length=15, unique=True)
    ipAdress = models.CharField(verbose_name='Ip-адрес', max_length=12,unique=True)
    printerModel = models.ForeignKey(PrinterModel, verbose_name='Модель принтера', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='Место расположения', on_delete=models.CASCADE)
    printerStatus = models.ForeignKey(PrinterStatus,verbose_name='Статус', on_delete=models.CASCADE)    
            
    
    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'
        
        def __str__(self):
            return self.serialNumber

    
                

