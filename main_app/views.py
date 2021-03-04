from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout, WorkoutType


def home(request):
    return render(request, 'home.html')

def index(request):
    workout = Workout.objects.all()
    print(workout)
    return render(request, 'workouts/index.html', { 'workout': workout })

class WorkoutCreate(CreateView):
    model = Workout
    fields = ['name', 'workout_type', 'workout_length', 'calories_burned', 'description', 'date']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

def detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['workout_type', 'workout_length', 'calories_burned', 'description']

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts/'