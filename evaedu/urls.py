"""Основной файл маршрутов проекта EvaEdu"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from evaedu.views import about  # Представление для страницы "О проекте"

urlpatterns = [
    # Страница администратора
    path('admin/', admin.site.urls),

    # Главная страница (онбординг)
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Разделы проекта
    path('cards/', include('cards.urls')),
    path('glossary/', include('glossary.urls')),
    path('quizzes/', include('quizzes.urls')),

    # Страница "О проекте" с формой обратной связи
    path('about/', about, name='about'),
]

# Обработка медиафайлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
