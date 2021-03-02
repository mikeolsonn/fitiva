from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # feed / dashboard
    path('workouts/', views.index, name='index'),
    # create a new workout
    path('workouts/create/', views.WorkoutCreate.as_view(), name='create'),
    # workout details
    path('workouts/<int:workout_id>/', views.detail, name='detail'),
    # update workout
    path('workouts/<int:workout_id>/update/', views.WorkoutUpdate.as_view(), name='workout_update'),
    # delete
    path('workouts/<int:workout_id>/delete/', views.WorkoutDelete.as_view(), name='workout_delete'),
]