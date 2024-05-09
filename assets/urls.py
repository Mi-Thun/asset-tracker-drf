from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet)
router.register(r'assignments', views.AssignmentViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'company', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]