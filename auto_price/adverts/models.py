from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.urls import reverse
from datetime import datetime
import random
import string
from users.models import User


year_now = datetime.now().year


class Advert(models.Model):
    slug = models.SlugField(max_length=100, unique=True, null=False, db_index=True, verbose_name='URL')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_adverts', verbose_name='Пользователь')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    price = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999999)], verbose_name='Цена')
    date_published = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, through='FavoriteAdvert', related_name='advert')

    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='auto_brand', verbose_name='Марка')
    model = models.ForeignKey('ModelAuto', on_delete=models.CASCADE, related_name='auto_model', verbose_name='Модель')
    year = models.IntegerField(validators=[MinValueValidator(1880), MaxValueValidator(year_now)], verbose_name='Год выпуска')
    mileage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999)], verbose_name='Пробег')
    hand_drive = models.ForeignKey('HandDrive', on_delete=models.CASCADE, verbose_name='Руль')
    power_engien = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5000)], verbose_name='Мощность двигателя')
    type_engien = models.ForeignKey('TypeEngien', on_delete=models.CASCADE, verbose_name='Тип двигателя')
    transmission = models.ForeignKey('Transmission', on_delete=models.CASCADE, verbose_name='Коробка передач')
    drive_unit = models.ForeignKey('DriveUnit', on_delete=models.CASCADE, verbose_name='Привод')
    body = models.ForeignKey('Body', on_delete=models.CASCADE, verbose_name='Тип кузова')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name='Цвет')
    volume = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)], verbose_name='Объем двигателя')
    broken = models.BooleanField(default=False, blank=True, verbose_name='Битый')

    def __str__(self):
        return f'Объявление #{self.pk} {self.brand} {self.model}'
    
    def get_absolute_url(self):
        return reverse("adverts:advert_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'
    
    def save(self, *args, **kwargs):
        s = string.ascii_lowercase + string.digits + '-_'
        s = ''.join(random.choices(s, k=4))
        self.slug = slugify(f'{self.brand.name}-{self.model.name}-{s}')
        super(Advert, self).save(*args, **kwargs)


class FavoriteAdvert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_user', verbose_name='Пользователь')
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='favorite_advert', verbose_name='Объявление')

    def __str__(self) -> str:
        return f'{self.user.username}-{self.advert}'
    
    class Meta:
        verbose_name = 'Избранные объявления'
        verbose_name_plural = 'Избранные объявления' 


class ImageAdvert(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=f'adverts/%Y/%m/%d')

    def __str__(self):
        return f'Фото к объявлению #{self.advert.pk}'
    
    class Meta:
        verbose_name = 'Фото объявлений'
        verbose_name_plural = 'Фото объявлений'


######
class Brand(models.Model):
    name = models.CharField('Марка', max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class ModelAuto(models.Model):
    name = models.CharField('Модель', max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
########


class HandDrive(models.Model):
    type_hand_drive = models.CharField('Руль', max_length=50)

    def __str__(self):
        return f'{self.type_hand_drive}'

    class Meta:
        verbose_name = 'Руль'
        verbose_name_plural = 'Руль'


class TypeEngien(models.Model):
    type_engien = models.CharField('Тип двигателя', max_length=50)

    def __str__(self):
        return f'{self.type_engien}'

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Тип двигателя'


class Transmission(models.Model):
    type_transmission = models.CharField('Трансмиссия', max_length=50)

    def __str__(self):
        return f'{self.type_transmission}'

    class Meta:
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Трансмиссия'


class DriveUnit(models.Model):
    type_drive_unit = models.CharField('Привод', max_length=50)

    def __str__(self):
        return f'{self.type_drive_unit}'

    class Meta:
        verbose_name = 'Привод'
        verbose_name_plural = 'Привод'


class Body(models.Model):
    type_body = models.CharField('Тип кузова', max_length=50)

    def __str__(self):
        return f'{self.type_body}'

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Тип кузова'


class Color(models.Model):
    color = models.CharField('Цвет', max_length=50)

    def __str__(self):
        return f'{self.color}'

    class Meta:
        verbose_name = 'Цвета'
        verbose_name_plural = 'Цвет'

