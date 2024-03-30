from django import forms
from cars.models import *


class SmallFilterForm(forms.ModelForm):

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        empty_label="Не выбрано",
        label="Марка",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )
    model = forms.ModelChoiceField(
        queryset=ModelAuto.objects.all(),
        empty_label="Не выбрано",
        label="Модель",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )
    year = forms.IntegerField(
        label="Год", widget=forms.NumberInput(attrs={"class": "input-group"})
    )
    transmission = forms.ModelChoiceField(
        queryset=Transmission.objects.all(),
        empty_label="Не выбрано",
        label="КПП",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    class Meta:
        model = Car
        fields = ["brand", "model", "transmission", "year"]