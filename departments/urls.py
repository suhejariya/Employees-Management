from django.urls import path
from .views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView, DepartmentDetailView

app_name = "departments"

urlpatterns = [
    path('department-list/', DepartmentListView.as_view(), name='department-list'),
    path('department-create/', DepartmentCreateView.as_view(), name='department-create'),
    path('department-update/<int:pk>/', DepartmentUpdateView.as_view(), name='department-update'),
    path('department-delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('department-detail/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]
