from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'limits', views.LimitViewSet)
router.register(r'users', views.UserViewSet)


appname = 'api'
urlpatterns = [
    path('', include(router.urls))
]