from django import forms

from .models import Mailing


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...'})
        }
