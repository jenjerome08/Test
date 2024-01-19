from django.urls import path
from . import views

urlpatterns = [
    path ('', views.homePage, name="homePage"),
    path ('about/', views.aboutPage, name="aboutPage"),
    path ('profile/<int:pk>/', views.profilePage, name="profilePage"),
    path('track/<int:pk>/', views.trackPage, name="trackPage"),
    path ('create_musician/', views.createMusicianPage, name="createMusicianPage"),
    path('update_musician/<int:pk>/', views.updateMusician, name="updateMusician"),
    path('delete_musician/<int:pk>/', views.deleteMusician, name="deleteMusician"),

]
