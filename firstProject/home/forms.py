from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10)
    comment = forms.CharField(max_length=10000)
