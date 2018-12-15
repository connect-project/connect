from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=39, required=False,
                                 help_text="Enter First Name(optional)")
    last_name = forms.CharField(max_length=39, required=False,
                                 help_text="Enter last Name(optional)")
    email = forms.CharField(max_length=254,
                                 help_text="Enter your email(* required)")

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')
