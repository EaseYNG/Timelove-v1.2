from django.urls import path

from apps.accounts import views

# /login/
urlpatterns = [
    path('signup/', views.create_user, name='create_user'),
    path('display/', views.display_users, name='display_users'),
    path('', views.login, name='login'),
]