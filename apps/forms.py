from django import forms
from . models import list


class listFrom(forms.ModelForm):
    class Meta:
        model = list
        fields = [
            'english',
            'bangla',
            'count'
        ]
