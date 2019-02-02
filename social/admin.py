from django.contrib import admin

from social.models import (
    Comment,
    Connection,
    Like,
    UserProfile,
    UserPost,
)

class UserPostInline(admin.TabularInline):
    model = UserPost

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    filedsets = (
        ('Profile', {
            'fields': ('username', ('first_name', 'last_name'), 'email')
        })
    )
    inlines = [UserPostInline]
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'website')
    list_filter = ('is_active', 'is_staff')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    pass
