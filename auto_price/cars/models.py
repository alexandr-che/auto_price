# from django.contrib.postgres.fields import ArrayField
# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
# from datetime import datetime
# from django.urls import reverse


# year_now = datetime.now().year


# class Brand(models.Model):
#     name = models.CharField('Марка', max_length=50)
#     model = models.ForeignKey('ModelAuto', on_delete=models.CASCADE, verbose_name='Модель')

#     def __str__(self):
#         return f'{self.name}'

#     class Meta:
#         verbose_name = 'Марка'
#         verbose_name_plural = 'Марки'


# class ModelAuto(models.Model):
#     name = models.CharField('Модель', max_length=50)

#     def __str__(self):
#         return f'{self.name}'

#     class Meta:
#         verbose_name = 'Модель'
#         verbose_name_plural = 'Модели'


# class Car(models.Model):
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='brands', verbose_name='Марка')
#     model = models.ForeignKey(ModelAuto, on_delete=models.SET_NULL, null=True, related_name='models', verbose_name='Модель')
#     year = models.IntegerField(validators=[MinValueValidator(1880), MaxValueValidator(year_now)], verbose_name='Год выпуска')
#     mileage = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Пробег')
#     hand_drive = models.ForeignKey('HandDrive', on_delete=models.SET_NULL, null=True, verbose_name='Руль')
#     power_engien = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5000)], verbose_name='Мощность двигателя')
#     type_engien = models.ForeignKey('TypeEngien', on_delete=models.SET_NULL, null=True, verbose_name='Тип двигателя')
#     transmission = models.ForeignKey('Transmission', on_delete=models.SET_NULL, null=True, verbose_name='Коробка передач')
#     drive_unit = models.ForeignKey('DriveUnit', on_delete=models.SET_NULL, null=True, verbose_name='Привод')
#     body = models.ForeignKey('Body', on_delete=models.SET_NULL, null=True, verbose_name='Тип кузова')
#     color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
#     volume = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)], verbose_name='Объем двигателя')
#     broken = models.BooleanField(verbose_name='Битый', blank=True)

#     def __str__(self):
#         return f'{self.brand} {self.model} | ID: {self.pk}'
    
#     def get_absolute_url(self):
#         return reverse("cars:car", kwargs={"slug": self.slug})
    
#     class Meta:
#         verbose_name = 'Автомобиль'
#         verbose_name_plural = 'Автомобили'


# class ImageAuto(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images', verbose_name='Фото')
#     image = models.ImageField(
#         upload_to=f'images/%Y/%m/%d',
#         validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
#         )


# class HandDrive(models.Model):
#     type_hand_drive = models.CharField('Руль', max_length=50)

#     def __str__(self):
#         return f'{self.type_hand_drive}'

#     class Meta:
#         verbose_name = 'Руль'
#         verbose_name_plural = 'Руль'


# class TypeEngien(models.Model):
#     type_engien = models.CharField('Тип двигателя', max_length=50)

#     def __str__(self):
#         return f'{self.type_engien}'

#     class Meta:
#         verbose_name = 'Тип двигателя'
#         verbose_name_plural = 'Тип двигателя'


# class Transmission(models.Model):
#     type_transmission = models.CharField('Трансмиссия', max_length=50)

#     def __str__(self):
#         return f'{self.type_transmission}'

#     class Meta:
#         verbose_name = 'Трансмиссия'
#         verbose_name_plural = 'Трансмиссия'


# class DriveUnit(models.Model):
#     type_drive_unit = models.CharField('Привод', max_length=50)

#     def __str__(self):
#         return f'{self.type_drive_unit}'

#     class Meta:
#         verbose_name = 'Привод'
#         verbose_name_plural = 'Привод'


# class Body(models.Model):
#     type_body = models.CharField('Тип кузова', max_length=50)

#     def __str__(self):
#         return f'{self.type_body}'

#     class Meta:
#         verbose_name = 'Тип кузова'
#         verbose_name_plural = 'Тип кузова'


# class Color(models.Model):
#     color = models.CharField('Цвет', max_length=50)

#     def __str__(self):
#         return f'{self.color}'

#     class Meta:
#         verbose_name = 'Цвета'
#         verbose_name_plural = 'Цвет'

