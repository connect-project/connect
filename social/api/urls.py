# pylint: disable=invalid-name
from django.urls import path

from social.api import views


app_name = 'social-api'

urlpatterns = [
    path('users_all/', views.ListUserProfilesView.as_view(), name='users-all'),
]
