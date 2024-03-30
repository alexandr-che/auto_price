# from django import forms
# from cars.models import *



# class CreateAdvertForm(forms.ModelForm):

#     brand = forms.ModelChoiceField(
#         queryset=Brand.objects.all(),
#         empty_label="Не выбрано",
#         label="Марка",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select"
#             }
#         ),
#     )
#     model = forms.ModelChoiceField(
#         queryset=ModelAuto.objects.all(),
#         empty_label="Не выбрано",
#         label="Модель",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select"
#             }
#         ),
#     )
#     year = forms.IntegerField(
#         label="Год",
#         widget=forms.NumberInput(attrs={"class": "form-control"})
#     )
#     mileage = forms.IntegerField(
#         label="Пробег", widget=forms.NumberInput(attrs={"class": "form-control"})
#     )
#     hand_drive = forms.ModelChoiceField(
#         queryset=HandDrive.objects.all(),
#         empty_label="Не выбрано",
#         label="Руль",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#             }
#         ),
#     )
#     type_engien = forms.ModelChoiceField(
#         queryset=TypeEngien.objects.all(),
#         empty_label="Не выбрано",
#         label="Тип топлива",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#             }
#         ),
#     )
#     volume = forms.FloatField(
#         label="Объем двигателя",
#         widget=forms.NumberInput(
#             attrs={
#                 "class": "form-control",
#             }
#         ),
#     )
#     transmission = forms.ModelChoiceField(
#         queryset=Transmission.objects.all(),
#         empty_label="Не выбрано",
#         label="КПП",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#             }
#         ),
#     )
#     drive_unit = forms.ModelChoiceField(
#         queryset=DriveUnit.objects.all(),
#         empty_label="Не выбрано",
#         label="Привод",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#             }
#         ),
#     )
#     body = forms.ModelChoiceField(
#         queryset=Body.objects.all(),
#         empty_label="Не выбрано",
#         label="Кузов",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#             }
#         ),
#     )
#     color = forms.ModelChoiceField(
#         queryset=Color.objects.all(),
#         empty_label="Не выбрано",
#         label="Цвет",
#         widget=forms.Select(
#             attrs={
#                 "class": "form-select",
#             }
#         ),
#     )
#     description = forms.CharField(
#         label="Описание", widget=forms.Textarea(attrs={"class": "form-control"})
#     )
#     broken = forms.BooleanField(
#         required=False,
#         label="Битый", widget=forms.CheckboxInput(attrs={"class": "form-check"})
#     )
#     price = forms.IntegerField(
#         label="Цена", widget=forms.NumberInput(attrs={"class": "form-control"})
#     )
#     power_engien = forms.IntegerField(
#         label="Мощность двигателя (Л.С.)",
#         widget=forms.NumberInput(attrs={"class": "form-control"})
#     )


#     class Meta:
#         model = Car
#         exclude = ["slug", "date_published"]