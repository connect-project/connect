from django.contrib import admin

from social.models import (
    Comment,
    Connection,
    Like,
    UserProfile,
    UserPost,
)

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Connection)
admin.site.register(Like)
admin.site.register(UserPost)
