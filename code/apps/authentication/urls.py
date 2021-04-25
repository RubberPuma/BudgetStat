from django.urls import path

from . import views

appname = "authentication"
urlpatterns = [
    path("auth/register", views.register_request, name="register"),
    path("auth/login", views.login_request, name="login"),
    path("auth/logout", views.logout_request, name="logout"),
    # temporary url for testing
    path("auth/dashboard", views.dashboard, name="dashboard"),
]
