from django.urls import path

from apps.anniversary import views


urlpatterns = [
    path('add/', views.create_anniversary, name='add_anniversary'),
    path('display/', views.db_display_anniversaries, name='display_anniversaries'),
    path('edit/', views.edit_anniversary, name='edit_anniversary'),
]