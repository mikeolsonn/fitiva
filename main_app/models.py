from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TYPES = (
    ('a', 'run'),
    ('b', 'ride'),
    ('c', 'walk'),
    ('d', 'run'),
    ('e', 'ride'),
    ('f', 'walk'),
    ('g', 'hike'),
    ('h', 'canoe'),
    ('i', 'weight training'),
    ('j', 'swim'),
    ('k', 'cross-fit'),
    ('l', 'stairs-stepper'),
    ('m', 'elliptical'),
    ('n', 'workout - other'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})
    
    class Meta:
        ordering = ['-date']

