from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required, login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Book, Library, UserProfile
from .forms import RegisterForm, BookForm

# --- Task 1: Function-based view to list all books ---
def list_books(request):
    books = Book.objects.select_related('author').all()
        return render(request, 'list_books.html', {'books': books})

        # --- Task 1: Class-based view to show library details ---
        class LibraryDetailView(DetailView):
            model = Library
                template_name = 'library_detail.html'
                    context_object_name = 'library'

                    # --- Task 2: Authentication views ---
                    class AppLoginView(LoginView):
                        template_name = 'relationship_app/login.html'

                        class AppLogoutView(LogoutView):
                            template_name = 'relationship_app/logout.html'

                            def register(request):
                                if request.method == 'POST':
                                        form = RegisterForm(request.POST)
                                                if form.is_valid():
                                                            user = form.save()
                                                                        # user.profile created by signal; optionally set role here
                                                                                    login(request, user)
                                                                                                return redirect('list_books')
                                                                                                    else:
                                                                                                            form = RegisterForm()
                                                                                                                return render(request, 'relationship_app/register.html', {'form': form})

                                                                                                                # --- Task 3: role-check helpers ---
                                                                                                                def is_admin(user):
                                                                                                                    return hasattr(user, 'profile') and user.profile.role == UserProfile.ROLE_ADMIN

                                                                                                                    def is_librarian(user):
                                                                                                                        return hasattr(user, 'profile') and user.profile.role == UserProfile.ROLE_LIBRARIAN

                                                                                                                        def is_member(user):
                                                                                                                            return hasattr(user, 'profile') and user.profile.role == UserProfile.ROLE_MEMBER

                                                                                                                            # Role-based views
                                                                                                                            @user_passes_test(is_admin, login_url=reverse_lazy('login'))
                                                                                                                            def admin_view(request):
                                                                                                                                return render(request, 'admin_view.html')

                                                                                                                                @user_passes_test(is_librarian, login_url=reverse_lazy('login'))
                                                                                                                                def librarian_view(request):
                                                                                                                                    return render(request, 'librarian_view.html')

                                                                                                                                    @user_passes_test(is_member, login_url=reverse_lazy('login'))
                                                                                                                                    def member_view(request):
                                                                                                                                        return render(request, 'member_view.html')

                                                                                                                                        # --- Task 4: Views with permission checks for book add/edit/delete ---
                                                                                                                                        @permission_required('relationship_app.can_add_book', raise_exception=True)
                                                                                                                                        def add_book(request):
                                                                                                                                            if request.method == 'POST':
                                                                                                                                                    form = BookForm(request.POST)
                                                                                                                                                            if form.is_valid():
                                                                                                                                                                        form.save()
                                                                                                                                                                                    return redirect('list_books')
                                                                                                                                                                                        else:
                                                                                                                                                                                                form = BookForm()
                                                                                                                                                                                                    return render(request, 'book_form.html', {'form': form, 'action': 'Add'})

                                                                                                                                                                                                    @permission_required('relationship_app.can_change_book', raise_exception=True)
                                                                                                                                                                                                    def edit_book(request, pk):
                                                                                                                                                                                                        book = get_object_or_404(Book, pk=pk)
                                                                                                                                                                                                            if request.method == 'POST':
                                                                                                                                                                                                                    form = BookForm(request.POST, instance=book)
                                                                                                                                                                                                                            if form.is_valid():
                                                                                                                                                                                                                                        form.save()
                                                                                                                                                                                                                                                    return redirect('list_books')
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                form = BookForm(instance=book)
                                                                                                                                                                                                                                                                    return render(request, 'book_form.html', {'form': form, 'action': 'Edit'})

                                                                                                                                                                                                                                                                    @permission_required('relationship_app.can_delete_book', raise_exception=True)
                                                                                                                                                                                                                                                                    def delete_book(request, pk):
                                                                                                                                                                                                                                                                        book = get_object_or_404(Book, pk=pk)
                                                                                                                                                                                                                                                                            if request.method == 'POST':
                                                                                                                                                                                                                                                                                    book.delete()
                                                                                                                                                                                                                                                                                            return redirect('list_books')
                                                                                                                                                                                                                                                                                                return render(request, 'confirm_delete.html', {'object': book})
                                                                                                                                                                                                                                                                                                