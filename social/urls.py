from django.urls import path
from social import views


app_name = 'social'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
]
