"""Представления для раздела "Словарь": просмотр, добавление, детали термина."""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Term
from .forms import TermForm

def term_list(request):
    """Отображает список всех терминов.
    Дополнительно передаёт количество терминов в шаблон."""
    terms = Term.objects.all()
    count = terms.count()
    return render(request, 'glossary/term_list.html', {
        'terms': terms,
        'term_count': count
    })


def term_detail(request, pk):
    #Отображает детальную информацию о выбранном термине.
    term = get_object_or_404(Term, pk=pk)
    return render(request, 'glossary/term_detail.html', {'term': term})


def add_term(request):
    #Обработка формы добавления нового термина.
    #Поддерживает загрузку изображений и валидацию описания.
    if request.method == 'POST':
        form = TermForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Термин успешно добавлен!")
            return redirect('term_list')
    else:
        form = TermForm()

    return render(request, 'glossary/add_term.html', {'form': form})
