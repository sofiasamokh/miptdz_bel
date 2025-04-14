"""Представление для страницы "О проекте" и обработки формы обратной связи."""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

@csrf_exempt  # Отключаем проверку CSRF для учебных целей (не рекомендуется в продакшене)
def about(request):
    
    """Обрабатывает GET и POST-запросы на странице "О проекте".
    Если форма отправлена (POST), сохраняет имя пользователя, категорию и сообщение
    в файл feedback.txt. Далее отображает страницу about.html."""
    
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        category = request.POST.get('category')
        message = request.POST.get('message')

        # Сохраняем в текстовый файл с отметкой времени
        with open('feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f'[{now().strftime("%Y-%m-%d %H:%M")}] {name} ({category}):\n{message}\n\n')

    # Отображаем шаблон страницы "О проекте"
    return render(request, 'about.html')
