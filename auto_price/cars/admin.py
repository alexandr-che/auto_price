# from django.contrib import admin
# from cars.models import *

# admin.site.register(Brand)
# admin.site.register(ModelAuto)
# admin.site.register(HandDrive)
# admin.site.register(TypeEngien)
# admin.site.register(Transmission)
# admin.site.register(DriveUnit)
# admin.site.register(Body)
# admin.site.register(Color)


# class ImagesCarTabulareAdmin(admin.TabularInline):
#     model = ImageAuto


# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     fields = [
#         ('brand', 'model', 'year'),
#         ('mileage', 'volume', 'power_engien', 'transmission'),
#         ( 'body', 'hand_drive', 'type_engien'),
#         ('drive_unit', 'color', 'broken')
#     ]
#     list_display = [
#         'pk',
#         'brand',
#         'model',
#         'year',
#         'mileage',
#         ]
#     search_fields = [
#         'pk',
#         'brand',
#         'model'
#     ]
#     inlines = [ImagesCarTabulareAdmin]
