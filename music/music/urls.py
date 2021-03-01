"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views as home_view
from userauth import views as auth_views
from user_profile import views as profile_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.home_view, name='home'),
    path('register', auth_views.signup_view, name='register'),
    path('login', auth_views.login_view, name='login'),
    path('logout', auth_views.logout_view, name='logout'),
    path('profile', profile_view.profile_view, name='profile')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
