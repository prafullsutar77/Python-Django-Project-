from django import forms
from .models import LaptopModel,MobileModel,TvModel
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm) :
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password']

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=LaptopModel
        fields = '__all__'
    def clean_modelname(self):
        inputname = self.cleaned_data['modelname']
        if len(inputname) <= 20:
            return inputname
        else:
            raise forms.ValidationError('Modelname should bee less than or equal to 5')

    def clean_modelprice(self):
        inputprice=self.cleaned_data['modelprice']
        if int(inputprice)>=12000000:
            raise forms.ValidationError('Price should be less than 1.2 lac')
        else:
            return inputprice

    def clean_modelqnty(self):
        inputqnty=self.cleaned_data['modelqnty']
        if inputqnty >=10000000:
            raise forms.ValidationError('Qnty should be less than 20')
        else:
            return inputqnty


class MobileModelForm(forms.ModelForm):
    class Meta:
        model = MobileModel
        fields = '__all__'

class TvModelForm(forms.ModelForm):
    class Meta:
        model = TvModel
        fields = '__all__'









# class SignUpForm(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#     confirm_password=forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model=User
#         fields=['Username','Email','Password']
#
#     def clean(self):
#         cleaned_data = super(SignUpForm,self).clean()
#         password = cleaned_data.get("Password")
#         confirm_password = cleaned_data.get("Confirm_Password")
#
#     if password != confirm_password:
#         raise forms.ValidationError("Password & Confirm_Password does not match")
