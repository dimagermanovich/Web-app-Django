import django
from .models import table, tableIncapables
from django.forms import ModelForm, NumberInput, TextInput, DateInput


class tableForm(ModelForm):
    class Meta:
        model = table
        fields = ['incapable', 'number_of_list', 'name_of_organization', 'work', 'ache', 'begin_date', 'end_date']

        widgets = {
            'number_of_list': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of the disability certificate'
            }),
            'name_of_organization': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of med organization'
            }),
            'work': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post'
            }),
            'ache': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Disease'
            }),
            'begin_date': DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'placeholder': 'The beginning of the sick leave',
                'type': 'date'
            }),
            'end_date': DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'placeholder': 'The end of the sick leave',
                'type': 'date'
            }),
        }



class tableIncapablesForm(ModelForm):
    class Meta:
        model = tableIncapables
        fields = ['lastName', 'firstName', 'patronymic']

        widgets = {
            'lastName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'firstName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Patronymic'
            })
        }
