from django.urls import path, include
from . import views
from .views import list_books

urlpatterns = [
    # Task 1
    path('admin/', admin.site.urls),
        path('', include('relationship_app.urls')),  # root routes to app
        
        path('', views.list_books, name='list_books'),
            path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

                # Task 2 - auth
                    path('login/', views.AppLoginView.as_view(), name='login'),
                        path('logout/', views.AppLogoutView.as_view(), name='logout'),
                            path('register/', views.register, name='register'),

                                # Task 3 - role pages
                                    path('role/admin/', views.admin_view, name='admin_view'),
                                        path('role/librarian/', views.librarian_view, name='librarian_view'),
                                            path('role/member/', views.member_view, name='member_view'),

                                                # Task 4 - book management (permission-protected)
                                                    path('book/add/', views.add_book, name='add_book'),
                                                        path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
                                                            path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
                                                            ]
                                                            