from django import forms
from .models import Registration,Search
from django.forms import ModelForm
from django.shortcuts import reverse
import calendar


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    def get_absolute_url(self):
        return reverse('log_in')



YEAR = [x for x in range(1950, 2040)]
class SearchForm(forms.ModelForm):
    Booking_Date = forms.DateTimeField(widget=forms.SelectDateWidget(years=YEAR
            # attrs={
            #     'class': 'form-control',
            #     'placeholder': 'DateTime',
            # }
        ))
    class Meta:
        model = Search
        fields = ['Select_Place','Booking_Date']

