"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/albom', views.index),
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.moviedetailview),
    path('api/v1/register/',user_views.RegisterAPIVIEW.as_view()),
    path('api/v1/login/',user_views.LoginAPIView.as_view()),
    # path('api/v1/movies/cinemea/')
]
