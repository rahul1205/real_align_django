"""real_align_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from users import views as user_views

handler404 = user_views.splash_screen

urlpatterns = [
    url('^$', user_views.splash_screen),
    url('^admin', admin.site.urls),
    url('^login', user_views.login),
    url('^register', user_views.signup),
    url('^userprofile', user_views.userprofile)

]
