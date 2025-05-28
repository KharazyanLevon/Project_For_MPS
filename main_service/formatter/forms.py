__all__ = ()


from django import forms
from tinymce.widgets import TinyMCE
from .models import Text


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget = TinyMCE(attrs={'cols': 80, 'rows': 10})