from django.urls import path, include
from . import views

urlpatterns = [
    path('api/users/', views.UserList.as_view(), name='user-list'),
    path('api/teams/', views.TeamList.as_view(), name='team-list'),
    path('api/activity/', views.ActivityList.as_view(), name='activity-list'),
    path('api/leaderboard/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('api/workouts/', views.WorkoutList.as_view(), name='workout-list'),
    path('', views.api_root, name='api-root'),
]
