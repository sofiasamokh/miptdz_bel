"""Базовые настройки Django-проекта EvaEdu"""

from pathlib import Path
import os
from dotenv import load_dotenv  # Подключаем библиотеку для чтения переменных окружения

# Корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Загружаем переменные из .env файла
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Секретный ключ (загружается из .env)
SECRET_KEY = str(os.getenv("SECRET_KEY"))

# Режим отладки (тоже из .env)
DEBUG = os.getenv("DEBUG", "False") == "True"

# Разрешённые хосты (оставляем пустым для разработки)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1").split(",")

# Установленные приложения проекта
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Приложения проекта
    'cards',
    'glossary',
    'quizzes',
    'evaedu',
]

# Промежуточное ПО
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной URL-конфиг
ROOT_URLCONF = 'evaedu.urls'

# Настройки шаблонов
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

# WSGI-приложение
WSGI_APPLICATION = 'evaedu.wsgi.application'

# База данных (SQLite по умолчанию)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидаторы паролей (отключены для учебного проекта)
AUTH_PASSWORD_VALIDATORS = []

# Локализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Работа со статикой
STATIC_URL = 'static/'

# Настройки автоинкрементных ключей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Медиафайлы (загрузка изображений и файлов)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
