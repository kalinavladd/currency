from django import forms

from .models import ContactUs, Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ('name', 'source_url',)


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('email_from', 'subject', 'message')
