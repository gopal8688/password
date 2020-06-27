from django import forms
from .models import Registration
from django.forms import ModelForm
from django.shortcuts import reverse


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    def get_absolute_url(self):
        return reverse('log_in')
