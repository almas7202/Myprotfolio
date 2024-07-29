from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Name"}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Enter E-mail"}),
            'subject': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Subject"}),
            'message': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Message"}),
        }
