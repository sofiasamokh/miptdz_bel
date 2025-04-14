"""Представление для страницы викторины: отображение вопросов и проверка ответов."""

from django.shortcuts import render
from django.contrib import messages
from cards.models import Card
import random

def start_quiz(request):
    """Отображает викторину, формируя список вопросов из карточек с полями викторины.
    После отправки формы проверяет ответы и показывает результат."""
    cards = Card.objects.all()
    questions = []

    # Отбираем только карточки с заполненными данными для викторины
    for card in cards:
        if all([
            card.quiz_question,
            card.correct_answer,
            card.wrong_answer1,
            card.wrong_answer2
        ]):
            # Перемешиваем ответы для случайного порядка
            options = [card.correct_answer, card.wrong_answer1, card.wrong_answer2]
            random.shuffle(options)

            # Формируем вопрос для шаблона
            questions.append({
                'id': card.id,
                'question': card.quiz_question,
                'options': options,
                'correct': card.correct_answer
            })

    score = None

    # Обработка формы с ответами (POST-запрос)
    if request.method == 'POST':
        score = 0
        for q in questions:
            answer = request.POST.get(f"q{q['id']}")
            if answer == q['correct']:
                score += 1

        # Выводим результат через сообщения Django
        messages.success(request, f"Вы набрали {score} из {len(questions)}")

    # Отображаем страницу викторины с вопросами
    return render(request, 'quizzes/start_quiz.html', {
        'questions': questions
    })
