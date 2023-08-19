from django.urls import path, include

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskChangeStatusView,
)

task_patterns = [
    path("create", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
]

tag_patterns = [
    path("", TagListView.as_view(), name="tag-list"),
    path("create", TagCreateView.as_view(), name="tag-create"),
    path("<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/", include(task_patterns)),
    path("tags/", include(tag_patterns)),
    path("change_status/<int:pk>", TaskChangeStatusView.as_view(), name="task_change_status"),
]

app_name = "todo"
