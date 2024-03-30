from django.contrib import admin
from adverts.models import *

admin.site.register(FavoriteAdvert)
admin.site.register(ImageAdvert)
admin.site.register(Brand)
admin.site.register(ModelAuto)
admin.site.register(HandDrive)
admin.site.register(TypeEngien)
admin.site.register(Transmission)
admin.site.register(DriveUnit)
admin.site.register(Body)
admin.site.register(Color)


class ImagesAdvertTabulareAdmin(admin.TabularInline):
    model = ImageAdvert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    fields = [
        ('slug', 'user'),
        ('brand', 'year'),
        ('mileage', 'volume', 'power_engien', 'transmission'),
        ('body', 'hand_drive', 'type_engien'),
        ('drive_unit', 'color', 'broken'),
        ('price')
    ]
    list_display = [
        'pk',
        'user',
        'brand',
        'model',
        'year',
        'mileage',
        'price'
        ]
    search_fields = [
        'pk',
        'brand',
    ]
    inlines = [ImagesAdvertTabulareAdmin]
