# pylint: disable=invalid-name
from django.urls import path
from django.conf.urls import include

from social import views


app_name = 'social'

v1_api_patterns = [
    path('users_all/', views.ListUserProfilesView.as_view(), name='users-all'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    path('api/', include(v1_api_patterns)),
]
