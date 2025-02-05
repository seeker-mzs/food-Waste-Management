from django import forms
from .models import Donation, WasteTracking, Request
from django.contrib.auth.models import User

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['food_type', 'quantity', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

class WasteTrackingForm(forms.ModelForm):
    class Meta:
        model = WasteTracking
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['food_type', 'requested_quantity']  

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']