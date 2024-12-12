from django import forms
from .models import MensWearModel,KidsWearModel,WomenWearModel

class MensWearModelForm(forms.ModelForm):
    class Meta:
        model=MensWearModel
        fields = '__all__'

class WomenWearModelForm(forms.ModelForm):
    class Meta:
        model = WomenWearModel
        fields = '__all__'

class KidsWearModelForm(forms.ModelForm):
    class Meta:
        model = KidsWearModel
        fields = '__all__'