"""Форма для создания и редактирования обучающих карточек."""

from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    """Форма ModelForm для модели Card.
    Содержит поля для термина, описания, изображения и данных для викторины.
    Используются Bootstrap-виджеты и человеко-понятные метки"""
    class Meta:
        """Модель термина словаря, включающая описание и связанные термины."""
        model = Card
        fields = [
            'term',
            'definition',
            'image',
            'quiz_question',
            'correct_answer',
            'wrong_answer1',
            'wrong_answer2',
        ]
        labels = {
            'term': 'Название термина',
            'definition': 'Описание',
            'image': 'Изображение',
            'quiz_question': 'Вопрос для викторины',
            'correct_answer': 'Правильный ответ',
            'wrong_answer1': 'Неправильный ответ',
            'wrong_answer2': 'Неправильный ответ',
        }
        widgets = {
            'term': forms.TextInput(attrs={'class': 'form-control'}),
            'definition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'quiz_question': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_answer': forms.TextInput(attrs={'class': 'form-control'}),
            'wrong_answer1': forms.TextInput(attrs={'class': 'form-control'}),
            'wrong_answer2': forms.TextInput(attrs={'class': 'form-control'}),
        }
