from django.forms import ModelForm
from .models import Workout, Comment

# class WorkoutForm(ModelForm):
#   class Meta:
#     model = Workout
#     fields = ['*']

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']