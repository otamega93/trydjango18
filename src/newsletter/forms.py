from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullName', 'email']

    def clean_email(self):
        print(self.cleaned_data.get('email'))
        return "abc@gmail.com"
