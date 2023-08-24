from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView

app_name='tasks'

urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task-list'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
