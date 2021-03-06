# pylint: disable=invalid-name

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from social import views

urlpatterns = [
    path('', include('social.urls')),
    path('admin/', admin.site.urls),
    path('social/', RedirectView.as_view(url='')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),
    path('posts', views.UserPostListView.as_view(), name='posts-list'),
    path('api/social/', include('social.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
