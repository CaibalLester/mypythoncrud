from django import forms
from todolist.models import Todolist

class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['name', 'value', 'datetime_field', 'comments', 'username', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'datetime_field': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),  
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            return ''
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is None:
            return ''
        return password