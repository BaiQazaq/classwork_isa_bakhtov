from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    author = forms.CharField(max_length=10, required=True, label='Автор')
    text = forms.CharField(
        max_length=2000,
        required=True,
        label='Текст',
        widget=widgets.Textarea
        )
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2x символов')
        return title