from django import forms
from home.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields="__all__"
        exclude=["age"]
