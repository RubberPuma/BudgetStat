from django.urls import path
from . import views


appname = 'authentication'
urlpatterns = [
    path("register", views.register_request , name='register'),
    path("login", views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    # temporary url for testing
    path("dashboard", views.dashboard, name= "dashboard"),
]