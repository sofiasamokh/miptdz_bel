"""Модель вопроса для викторины."""

from django.db import models

class Question(models.Model):
    """Текст вопроса (обязательное поле, по умолчанию — пример)"""
    question_text = models.CharField(
        max_length=255,
        default="Пример вопроса"
    )

    # Варианты ответа (A, B, C, D)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    # Правильный вариант (одна из A, B, C, D)
    correct_option = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ]
    )

    def __str__(self):
        # Отображение вопроса в админке и консоли
        return str(self.question_text)
