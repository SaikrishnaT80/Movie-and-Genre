"""
URL configuration for MOVIES project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from movie.views import GenreView,MovieView,Genre_list_View,Genre_details_View,Genre_update_View,Movie_list_View,Movie_details_View,Movie_update_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genreadd/', GenreView.as_view(),name="g_add"),
    path('movieadd/', MovieView.as_view(),name="m_add"),
    path('genre_list/', Genre_list_View.as_view(),name="g_list"),
    path('genre_list/<int:pk>', Genre_details_View.as_view(),name="g_details"),
    path('genre_list/<int:pk>/update', Genre_update_View.as_view(),name="g_update"),
    path('movie_list/', Movie_list_View.as_view(),name="m_list"),
    path('movie_list/<int:pk>', Movie_details_View.as_view(),name="m_details"),
    path('movie_list/<int:pk>/update', Movie_update_View.as_view(),name="m_update"),
]
