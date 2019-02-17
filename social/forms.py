from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from social.models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=39, required=False,
                                 help_text="Optional. Enter First Name")
    last_name = forms.CharField(max_length=39, required=False,
                                help_text="Optional. Enter last Name")
    email = forms.CharField(max_length=254,
                            help_text="Required. Enter your email")
    website = forms.URLField(initial='http://', label="Website")
    photo = forms.ImageField(label="Upload your profile photo")

    bio = forms.CharField(
        max_length=UserProfile.USERPROFILE_BIO_MAX_LENGTH,
        required=False,
        help_text="Optional. Enter your bio.",
        widget=forms.Textarea)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'website',
            'bio',
        )
