from django import forms
from process.models import *
import random
from process.utils import sendTextMessage

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_otp(self):
        cno = self.cleaned_data['contact']
        #otp = self.cleaned_data['otp'] # 0
        otp = random.randint(100000,999999)
        message = 'Welcome to RMS and Your OTP is '+ str(otp)
        sendTextMessage(message,cno)
        return otp

    class Meta:
        model = RegistrationModel
        exclude = ('status',)

