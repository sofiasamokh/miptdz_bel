"""Форма для создания и редактирования терминов словаря."""

from django import forms
from .models import Term

class TermForm(forms.ModelForm):
    """Используем ModelForm для модели Term"""
    class Meta:
        """Модель для формы"""
        model = Term

        # Указываем поля, которые будут отображаться в форме
        fields = ['name', 'description', 'related_terms', 'image']

        # Подписи (labels), которые будут отображаться рядом с полями
        labels = {
            'name': 'Название термина',
            'description': 'Описание',
            'related_terms': 'Связанные термины',
            'image': 'Изображение',
        }

        # Стилизация полей с помощью Bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'related_terms': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    # Валидация описания: минимум 200 символов
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 200:
            raise forms.ValidationError('Описание должно содержать не менее 200 символов.')
        return description

    # Валидация уникальности названия (без учёта регистра)
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Term.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('Термин с таким названием уже существует.')
        return name
