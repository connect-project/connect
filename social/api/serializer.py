from rest_framework import serializers
from social.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "username",
            "first_name",
            "last_name",
            "bio",
            "website",
            "phone_number",
            "photo",
        )
