from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User=get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control form-control-lg'}),
            }