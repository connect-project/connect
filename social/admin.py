from django.contrib import admin

from social.models import (
    UserProfile,
    UserPosts,
    Connection,
)

admin.site.register(UserProfile)
