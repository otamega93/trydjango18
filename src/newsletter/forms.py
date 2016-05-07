from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullName', 'email']

    def clean_email(self):
        return self.cleaned_data.get('email')
