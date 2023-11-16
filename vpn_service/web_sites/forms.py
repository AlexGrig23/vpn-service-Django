from django import forms
from .models import WebSite


class WebSiteForm(forms.ModelForm):

    class Meta:
        model = WebSite
        fields = ['title', 'url']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }
