from datetime import date

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from django.utils.text import Truncator

from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    USERPROFILE_BIO_MAX_LENGTH = 400
    bio = models.TextField(
        max_length=USERPROFILE_BIO_MAX_LENGTH,
        help_text="You bio here!"
    )
    phone_number = PhoneNumberField()
    website = models.URLField(max_length=250)
    photo = models.ImageField(
        upload_to='upload/profile/',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["date_joined"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('polls:profile', kwargs={'username': self.username})

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def followers_count(self):
        return Connection.objects.filter(following=self).count()

    @property
    def following_count(self):
        return Connection.objects.filter(follower=self).count()

    def follow_user(self, userprofile, follow: bool):
        if follow:
            Connection.objects.get_or_create(
                follower=self, following=userprofile)
        else:
            Connection.objects.filter(
                follower=self, following=userprofile).delete()


def get_active_user(username: str):
    try:
        user = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return None
    if not user.is_active:
        return None
    return user


class Connection(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='follower',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='following',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["date_created"]

    def __str__(self):
        return f"{self.follower} : {self.following}"


class UserPostManager(models.Manager):
    def create_userpost(self, user_profile, text, **extra_fields):
        if not text:
            raise ValueError("User post can't be empty")
        userpost = self.model(user_profile=user_profile,
                              text=text, **extra_fields)
        userpost.save()
        return userpost


class UserPost(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        blank=True
    )
    date_posted = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)
    likes = models.IntegerField(default=0)
    PUBLIC = 1
    PRIVATE = 2
    PRIVACY_CHOICES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )
    privacy = models.PositiveSmallIntegerField(
        default=PUBLIC,
        choices=PRIVACY_CHOICES
    )

    USERPOST_TEXT_MAX_LENGTH = 1000
    text = models.TextField(
        max_length=USERPOST_TEXT_MAX_LENGTH,
        help_text="Your post here!"
    )

    objects = UserPostManager()

    class Meta:
        ordering = ["date_updated"]

    def get_number_of_likes(self):
        return self.like_set.count()

    def __str__(self):
        return f"Posted on {self.date_posted} : {Truncator(self.text).chars(50)}"


class Comment(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    commenter = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        blank=True
    )
    text = models.CharField(max_length=100)
    date_posted = models.DateField(default=date.today)

    def __str__(self):
        return f"Posted on {self.date_posted}. Comment: {self.text}"


class Like(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_post", "user_profile")
