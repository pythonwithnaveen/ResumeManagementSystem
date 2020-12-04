from django import forms
from process.models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        print("------",otp)
        return 5475

    class Meta:
        model = RegistrationModel
        exclude = ('status',)

