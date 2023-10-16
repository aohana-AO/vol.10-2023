from django import forms
from django.utils.translation import gettext_lazy
from . import models

User = models.User

class SearchForm(forms.Form):
    keywords = forms.CharField(
        label=gettext_lazy('keywords (split space)'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': gettext_lazy('Enter the room name.'),
            'class': 'form-control',
        }),
    )

    def get_keywords(self):
        init_keywords = ''
        keywords = init_keywords

        if self.is_valid():
            keywords = self.cleaned_data.get('keywords', init_keywords)

        return keywords

class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ('name','ChatGPT','Claude2','PaLM2','LLaMA')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': gettext_lazy('Enter the room name.'),
                'class': 'form-control',
            }),
            'ChatGPT': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox'
            }),
            'Claude2': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox'
            }),
            'PaLM2': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox'
            }),
            'LLaMA': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox'
            }),

        }

