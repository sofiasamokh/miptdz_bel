"""Регистрация модели Card в административной панели Django."""

from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Настройки отображения карточек в админке:
    - Показываются поля 'term' и 'created_at';
    - Реализован поиск по полям 'term', 'definition' и 'quiz_question'."""
    list_display = ('term', 'created_at')
    search_fields = ('term', 'definition', 'quiz_question')
