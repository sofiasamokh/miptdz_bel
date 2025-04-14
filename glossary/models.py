"""Модель словарного термина для раздела "Словарь" (glossary)."""

from django.db import models

class Term(models.Model):
    """Название термина (уникальное, не чувствительно к регистру в форме)"""
    name = models.CharField(max_length=100, unique=True)

    # Подробное описание термина
    description = models.TextField()

    # Связанные термины (можно указать другие Term, связанные по смыслу)
    related_terms = models.ManyToManyField("self", blank=True)

    # Изображение, иллюстрирующее термин (необязательное)
    image = models.ImageField(upload_to='term_images/', null=True, blank=True)

    def __str__(self):
        # Отображает название термина при выводе объекта
        return str(self.name)
