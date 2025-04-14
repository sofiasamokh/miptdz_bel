"""Регистрация модели Term в административной панели Django."""

from django.contrib import admin
from .models import Term

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    """Настройки отображения терминов в админке:
    - Отображается поле 'name' в списке;
    - Поиск доступен по полям 'name' и 'description'."""
    list_display = ('name',)
    search_fields = ('name', 'description')
