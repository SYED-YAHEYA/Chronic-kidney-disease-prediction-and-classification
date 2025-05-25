from django import forms 
from . models import UserPredictModel
from . models import Patient_info
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class UserPredictForm(forms.ModelForm):
    
    class Meta:
        model = UserPredictModel
        fields = ['image']


class Patient_info_Form(forms.ModelForm):
    class Meta:
        model = Patient_info
        fields = ['Bp', 'Sg', 'Al', 'Su', 'Rbc', 'Bu', 'Sc', 'Sod', 'Pot', 'Hemo', 'Wbcc', 'Rbcc', 'Htn']
