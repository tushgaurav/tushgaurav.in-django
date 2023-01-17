from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from .models import Message

class CreateUserForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'your name'})
        self.fields['username'].widget.attrs.update({'placeholder': 'your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'your email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'confirm password'})


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = Message 
        fields = ['content', 'contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder': 'Enter your message here'})
        self.fields['contact_number'].widget.attrs.update({'placeholder': "Enter your phone number here"})

    def save(self, commit=True, request=None):
        instance = super(ContactForm, self).save(commit=False)
        if request and request.user.is_authenticated:
            instance.user = request.user
        if commit:
            instance.save()
        return instance