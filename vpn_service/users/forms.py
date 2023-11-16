from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
        widgets = {

            'bio': forms.TextInput(attrs={'class': 'form-control'}),
        }
