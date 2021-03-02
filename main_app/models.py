from django.db import models
from django.urls import reverse
from datetime import date

TYPES = (
    ('a', 'run'),
    ('b', 'ride'),
    ('c', 'walk'),
)

class WorkoutType(models.Model):
    name = models.CharField(
        max_length=50,
        choices=TYPES,
        default=TYPES[0][0],
    )

class Workout(models.Model):
    name = models.CharField(max_length=250)
    workout_type = models.CharField(max_length=25)
    workout_length = models.IntegerField()
    calories_burned = models.IntegerField()
    description = models.TextField(max_length=500)
    date = models.DateField('workout date')

    def __str__(self):
        return self.name

