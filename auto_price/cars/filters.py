# import django_filters
# from django import forms
# from .models import *


# class SmallCarFilter(django_filters.FilterSet):
    
#     brand = django_filters.ModelChoiceFilter(
#         queryset=Brand.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     model = django_filters.ModelChoiceFilter(
#         queryset=ModelAuto.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     transmission = django_filters.ModelChoiceFilter(
#         queryset=Transmission.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     mileage = django_filters.RangeFilter(
#         field_name='mileage',
#         widget=django_filters.widgets.RangeWidget(attrs={"class": "form-control"})
#     )

#     price = django_filters.RangeFilter(
#         field_name='price',
#         widget=django_filters.widgets.RangeWidget(attrs={"class": "form-control"})
#     )

#     broken = django_filters.BooleanFilter(
#         widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
#     )


# class BigCarFilter(django_filters.FilterSet):

#     brand = django_filters.ModelChoiceFilter(
#         queryset=Brand.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     model = django_filters.ModelChoiceFilter(
#         queryset=ModelAuto.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     year = django_filters.RangeFilter(
#         field_name='year',
#         widget=django_filters.widgets.RangeWidget(attrs={"class": "form-control"})
#     )

#     mileage = django_filters.RangeFilter(
#         field_name='mileage',
#         widget=django_filters.widgets.RangeWidget(attrs={"class": "form-control"})
#     )

#     price = django_filters.RangeFilter(
#         field_name='price',
#         widget=django_filters.widgets.RangeWidget(attrs={"class": "form-control"})
#     )

#     type_engien = django_filters.ModelChoiceFilter(
#         queryset=TypeEngien.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     volume = django_filters.NumberFilter(
#         field_name='volume',
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )

#     power_engien = django_filters.NumberFilter(
#         field_name='power_engien',
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )

#     transmission = django_filters.ModelChoiceFilter(
#         queryset=Transmission.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     drive_unit = django_filters.ModelChoiceFilter(
#         queryset=DriveUnit.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     hand_drive = django_filters.ModelChoiceFilter(
#         queryset=HandDrive.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     body = django_filters.ModelChoiceFilter(
#         queryset=Body.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     color = django_filters.ModelChoiceFilter(
#         queryset=Color.objects.all(),
#         empty_label='Не выбрано',
#         widget=forms.Select(attrs={"class": "form-select"})
#     )

#     broken = django_filters.BooleanFilter(
#         widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
#     )





    


    