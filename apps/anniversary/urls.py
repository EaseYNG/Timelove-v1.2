from django.urls import path

from apps.anniversary import views


urlpatterns = [
    path('add/', views.create_anniversary, name='add_anniversary'),
]