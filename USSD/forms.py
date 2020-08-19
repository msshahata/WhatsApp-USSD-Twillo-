from django import forms
from django.contrib.auth.models import User
from .models import WhatsAppDetails,WhatsAppSendMSG


class WhatsAppDetailsForm(forms.ModelForm):
    class Meta():
        model = WhatsAppDetails
        fields = ('code','message')


class WhatsAppSendMSGForm(forms.ModelForm):
    class Meta():
        model = WhatsAppSendMSG
        fields = ('To','message')
    From = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='+14155238886')
