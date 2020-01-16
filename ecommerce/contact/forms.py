from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Contact
        fields = '__all__'
