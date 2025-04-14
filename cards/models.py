"""Модель обучающей карточки, содержащей термин, 
определение, изображение и данные для викторины"""

from django.db import models

class Card(models.Model):
    """Модель термина словаря, включающая описание и связанные термины."""
    term = models.CharField(max_length=100)

    # Подробное описание термина
    definition = models.TextField()

    # Изображение, связанное с карточкой (необязательное)
    image = models.ImageField(upload_to='card_images/', null=True, blank=True)

    # Дата и время создания карточки (проставляется автоматически)
    created_at = models.DateTimeField(auto_now_add=True)

    # Вопрос, связанный с этой карточкой (для использования в викторине)
    quiz_question = models.CharField(
        max_length=255,
        blank=True,
        help_text="Вопрос для викторины"
    )

    # Правильный и два неправильных варианта ответа
    correct_answer = models.CharField(max_length=30, blank=True)
    wrong_answer1 = models.CharField(max_length=30, blank=True)
    wrong_answer2 = models.CharField(max_length=30, blank=True)

    # Возвращает название термина в интерфейсе администратора и при печати объекта
    def __str__(self):
        return str(self.term)
