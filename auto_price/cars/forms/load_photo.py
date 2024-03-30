from django import forms
from cars.models import ImageAuto


class LoadPhotoForm(forms.ModelForm):
    class Meta:
        model = ImageAuto
        fields = ['image']