from rest_framework import generics

from social.api.serializer import UserProfileSerializer
from social.models import (
    UserProfile,
)


class ListUserProfilesView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
