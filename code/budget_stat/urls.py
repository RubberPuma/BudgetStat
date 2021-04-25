"""budget_stat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from apps.authentication.views import UserViewSet
from apps.categories.views import CategoryViewSet
from apps.expenses.views import ExpenseViewSet
from apps.limits.views import LimitViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"expenses", ExpenseViewSet)
router.register(r"limits", LimitViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", include("apps.authentication.urls")),
    path("admin/", admin.site.urls),
    path("dashboard/", include("apps.frontend.urls")),
]

admin.site.site_header = "BudgetStat"
