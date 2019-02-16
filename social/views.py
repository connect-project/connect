from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest, HttpResponse
)
from django.shortcuts import redirect, render

from social.forms import SignUpForm
from social.models import (
    UserProfile
)


def signup(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('social:home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('social:home')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'home.html',
    )


@login_required
def profile(request: HttpRequest, username: str) -> HttpResponse:
    user = UserProfile.objects.get(username=username)
    if not user:
        return redirect('social:home')

    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)
