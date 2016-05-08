from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    fullName = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullName', 'email']

    def clean_email(self):
        return self.cleaned_data.get('email')
