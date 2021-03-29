from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Workout
from .forms import CommentForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    
@login_required
def index(request):
    workout = Workout.objects.all()
    print(workout)
    return render(request, 'workouts/index.html', { 'workout': workout })

@login_required
def detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    comment_form = CommentForm()
    return render(request, 'workouts/detail.html', { 'workout': workout, 'comment_form': comment_form })

@login_required
def myworkouts(request):
    workout = Workout.objects.all()
    print(workout)
    return render(request, 'workouts/myworkouts.html', { 'workout': workout })

@login_required
def add_comment(request, workout_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.workout_id = workout_id
        new_comment.author = request.user
        new_comment.save()
    return redirect('detail', workout_id=workout_id)

class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['name', 'workout_type', 'workout_length', 'calories_burned', 'description', 'date']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    


class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['workout_type', 'workout_length', 'calories_burned', 'description']
    

class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = '/workouts/'
