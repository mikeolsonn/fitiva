from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout, WorkoutType


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'

def detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = '__all__'
    success_url = '/workouts/'

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts/'