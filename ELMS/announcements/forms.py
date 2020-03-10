from django import forms

from .models import Announcements


class CreateAnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'content']
        