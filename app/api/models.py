from django.db import models


class Car(models.Model):
    FUEL_CHOICES = [
        ('бензин', 'Бензин'),
        ('дизель', 'Дизель'),
        ('электричество', 'Электричество'),
        ('гибрид', 'Гибрид'),
    ]

    TRANSMISSION_CHOICES = [
        ('механическая', 'Механическая'),
        ('автоматическая', 'Автоматическая'),
        ('вариатор', 'Вариатор'),
        ('робот', 'Робот'),
    ]

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=15, choices=FUEL_CHOICES)
    transmission = models.CharField(
        max_length=15, choices=TRANSMISSION_CHOICES)
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'
