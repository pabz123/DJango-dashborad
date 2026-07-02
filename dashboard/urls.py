from django.urls import path
from . import views

urlpatterns = [
    # function-based views
    path('', views.dashboard, name='dashboard'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('add-task/', views.add_task, name='add_task'),

    # API endpoints
    path('api/tasks/', views.TaskListCreateAPI.as_view(), name='task-list-api'),
    path('api/tasks/<int:pk>/', views.TaskDetailAPI.as_view(), name='task-detail-api'),

    # CBV-based post CRUD
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]