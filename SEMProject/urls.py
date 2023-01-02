"""SEMProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import include
from App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage),
    path('aboutus/', views.aboutus),
    path('eventbookform/', views.bookevent_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),
    path('signup/',views.signup_view),
    re_path('^.*$', views.homepage), #dont use re_path() for def/any-url


]
