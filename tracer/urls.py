"""tracer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import ConfirmEmailView
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from tracer.profiles import views as profiles_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    # path('rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
    #     ConfirmEmailView.as_view(),
    #     name='account_confirm_email'),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # path('', profiles_views.IndexView.as_view(), name='index'),
    path('', profiles_views.ProfileView.as_view(), name='index'),
    path(
        'profile/<int:pk>/',
        profiles_views.ProfileDetailView.as_view(),
        name='profile-detail'),
    path(
        'profile/<int:pk>/update/',
        profiles_views.ProfileUpdateView.as_view(),
        name='profile-update'),

    path(
        'survey/',
        profiles_views.SurveyCreateView.as_view(),
        name='survey-create'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
