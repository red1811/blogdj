from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/<pk>/show', views.show_profile, name='show_profile'),
]
