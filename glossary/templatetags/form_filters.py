# Пользовательский шаблонный фильтр Django для добавления CSS-класса к полям формы

from django import template
from django.forms.boundfield import BoundField

# Регистрируем библиотеку фильтров
register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Добавляет указанный CSS-класс к полю формы в шаблоне.
    #Используется как фильтр: {{ form.field|add_class:"form-control" }}"""
    if isinstance(field, BoundField):
        # Возвращаем поле с новым классом
        return field.as_widget(attrs={'class': css_class})
    return field  # Если поле не BoundField, возвращаем его без изменений
