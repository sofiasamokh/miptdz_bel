"""URL-маршруты для раздела глоссарий."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.term_list, name='term_list'),  # Эта строка отвечает за список терминов
    path('add/', views.add_term, name='add_term'),  # Для добавления терминов
    path('<int:pk>/', views.term_detail, name='term_detail'),  # Для подробной информации о термине
]
