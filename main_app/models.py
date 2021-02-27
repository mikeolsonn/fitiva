from django.db import models
from datetime import date

# Create your models here

TYPES = (
    ('run'),
    ('ride'),
    ('walk'),
    ('hike'),
    ('canoe'),
    ('weight training'),
    ('swim'),
    ('cross-fit'),
    ('stairs-stepper'),
    ('elliptical'),
    ('workout - other'),
)

class Workout(models.Model):
    name = models.CharField(max_length=250)
    workout_type = models.ForeignKey(WorkoutType)
    workout_length = models.IntegerField()
    calories_burned = models.IntegerField()
    description = models.TextField(max_length=500)
    date = models.DateField('workout date')

class WorkoutType(models.Model):
    name = models.CharField(
        max_length=50,
        choices=TYPES,
        default=TYPES[0],
    )
