from django.forms import ModelForm
from .models import InterviewForm
from django import forms


class FormUser(forms.ModelForm):
    class Meta:
        model = InterviewForm
        fields = ['first_name', 'last_name', 'age', 'date_of_birth', 'candidate_cv', 'phone_number', 'picture']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'candidate_cv': forms.FileInput(attrs={'class': 'form-control-file'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }







