from django import forms

from .models import Handouts


class HandoutsForm(forms.ModelForm):
    class Meta:
        model = Handouts
        fields = ['name', 'documents', 'description']



