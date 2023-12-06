from django import forms
from todolist.models import Todolist

class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['name', 'value', 'datetime_field', 'comments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'datetime_field': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'})

        }
