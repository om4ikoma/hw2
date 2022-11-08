"""afisha URL Configuration

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
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', about_us),
    path('', films_list_view),
    path('date_now/', date_now),
    path('films/', films_list_view),
    path('films/<int:id>/', film_view),
    path('director/<int:director_id>/films/', director_films),
    path('director/create/', create_director),
    path('film/create/', create_film),
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_view),
    path('search/', search)
]
