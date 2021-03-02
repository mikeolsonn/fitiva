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
    return render(request, 'detail.html')

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = '__all__'

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts/'