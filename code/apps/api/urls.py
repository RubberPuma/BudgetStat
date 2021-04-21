from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"expenses", views.ExpenseViewSet)
router.register(r"limits", views.LimitViewSet)
router.register(r"users", views.UserViewSet)


appname = "api"
urlpatterns = [path("", include(router.urls))]
