from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library 

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
        return render(request, "relationship_app/list_books.html", {"books": books})

        # Class-based view: Library details
        class LibraryDetailView(DetailView):
            model = Library
                template_name = "relationship_app/library_detail.html"
                    context_object_name = "library"

                    # Role-based access control
                    def check_role(user, role):
                        return hasattr(user, "profile") and user.profile.role == role

                        @user_passes_test(lambda u: check_role(u, "Admin"))
                        def admin_view(request):
                            return render(request, "relationship_app/admin_view.html")

                            @user_passes_test(lambda u: check_role(u, "Librarian"))
                            def librarian_view(request):
                                return render(request, "relationship_app/librarian_view.html")

                                @user_passes_test(lambda u: check_role(u, "Member"))
                                def member_view(request):
                                    return render(request, "relationship_app/member_view.html")

                                    # Permission-protected views
                                    @permission_required("relationship_app.can_add_book")
                                    def add_book(request):
                                        return HttpResponse("You can add a book.")

                                        @permission_required("relationship_app.can_change_book")
                                        def edit_book(request):
                                            return HttpResponse("You can edit a book.")

                                            @permission_required("relationship_app.can_delete_book")
                                            def delete_book(request):
                                                return HttpResponse("You can delete a book.")
