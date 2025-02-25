from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)  # Название курса
    description = models.TextField(blank=True)  # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена курса

    def __str__(self):
        return self.title