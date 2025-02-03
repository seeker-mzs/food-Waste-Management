from django import forms
from .models import Donation, WasteTracking, Request
from django.contrib.auth.models import User

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__' 

class WasteTrackingForm(forms.ModelForm):
    class Meta:
        model = WasteTracking
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']