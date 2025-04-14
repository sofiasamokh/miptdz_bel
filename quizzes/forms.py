"""Форма для создания и редактирования вопросов викторины."""

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    """Форма ModelForm для модели Question.
    Позволяет вводить текст вопроса, варианты ответов и правильный ответ."""
    class Meta:
        model = Question
        fields = [
            'question_text',
            'option_a',
            'option_b',
            'option_c',
            'option_d',
            'correct_option',
        ]

        # Подписи для отображения в HTML-форме
        labels = {
            'question_text': 'Текст вопроса',
            'option_a': 'Вариант А',
            'option_b': 'Вариант B',
            'option_c': 'Вариант C',
            'option_d': 'Вариант D',
            'correct_option': 'Правильный вариант (A, B, C или D)',
        }

        # Виджеты для стилизации через Bootstrap
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'option_a': forms.TextInput(attrs={'class': 'form-control'}),
            'option_b': forms.TextInput(attrs={'class': 'form-control'}),
            'option_c': forms.TextInput(attrs={'class': 'form-control'}),
            'option_d': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_option': forms.TextInput(attrs={'class': 'form-control'}),
        }
