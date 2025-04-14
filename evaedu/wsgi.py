"""WSGI-конфигурация для запуска проекта EvaEdu"""

import os
from django.core.wsgi import get_wsgi_application

# Устанавливаем модуль настроек Django по умолчанию
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaedu.settings')

# Получаем объект WSGI-приложения для запуска сервера
application = get_wsgi_application()
