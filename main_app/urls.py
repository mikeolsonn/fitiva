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
    # my workout details
    path('workouts/myworkouts/', views.myworkouts, name='myworkouts'),
    # update workout
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout_update'),
    # delete
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout_delete'),
    # signup 
    path('accounts/signup/', views.signup, name='signup'),
    # comment
    path('workouts/<int:workout_id>/add_comment/', views.add_comment, name='comment'),
]