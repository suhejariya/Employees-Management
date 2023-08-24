from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from employees.models import Employee
from departments.models import Department
from tasks.models import Task

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'name': ['icontains'],
            'department__name': ['icontains'],
        }

class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            'name': ['icontains'],
        }

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'assigned_to__name': ['icontains'],
        }
