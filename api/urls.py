from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
