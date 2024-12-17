from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название доски")
    description = models.TextField(blank=True, verbose_name="Описание")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_boards", verbose_name="Владелец")
    members = models.ManyToManyField(User, related_name="boards", blank=True, verbose_name="Участники")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название колонки")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="columns", verbose_name="Доска")
    position = models.PositiveIntegerField(verbose_name="Позиция")

    def __str__(self):
        return f"{self.name} ({self.board.name})"


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание")
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="tasks", verbose_name="Колонка")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks",
                                    verbose_name="Ответственный")
    due_date = models.DateField(null=True, blank=True, verbose_name="Срок выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    position = models.PositiveIntegerField(verbose_name="Позиция в колонке")

    def __str__(self):
        return self.title
