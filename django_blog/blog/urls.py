from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
        path('search/', views.PostListView.as_view(), name='search'),
            path('tags/<str:tag>/', views.PostListView.as_view(), name='posts_by_tag'),
                path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
                    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
                        path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
                            path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
                                path('posts/<int:pk>/comments/add/', views.add_comment, name='add_comment'),
                                    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
                                        path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
                                            # auth
                                                path('register/', views.register, name='register'),
                                                    path('profile/', views.profile, name='profile'),
                                                    ]
                                                    