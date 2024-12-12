from django import forms
from .models import SliperModel,SportsModel,ShoesModel

class SliperModelForm(forms.ModelForm):
    class Meta:
        model=SliperModel
        fields="__all__"

class SportsModelForm(forms.ModelForm):
    class Meta:
        model=SportsModel
        fields="__all__"

class ShoesModelForm(forms.ModelForm):
    class Meta:
        model=ShoesModel
        fields="__all__"