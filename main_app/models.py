from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TYPES = (
    ('run', 'run'),
    ('ride', 'ride'),
    ('walk', 'walk'),
    ('hike', 'hike'),
    ('canoe', 'canoe'),
    ('weight training', 'weight training'),
    ('swim', 'swim'),
    ('cross-fit', 'cross-fit'),
    ('stairs-stepper', 'stairs-stepper'),
    ('elliptical', 'elliptical'),
    ('workout - other', 'workout - other'),
)

class Workout(models.Model):
    name = models.CharField(max_length=250)
    workout_type = models.CharField(
        max_length=50,
        choices=TYPES,
        default=TYPES[0][1],
    )
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

class Comment(models.Model):
    comment = models.TextField(max_length=120)
    date =  models.DateField(auto_now_add=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} on {self.date} by {self.author.username}"
        
    class Meta:
        ordering = ['-date']