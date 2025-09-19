from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms


# Secure form validation instead of raw request.POST usage
class BookForm(forms.ModelForm):
    class Meta:
            model = Book
                    fields = ["title", "author", "published_date"]


                    @permission_required("bookshelf.can_view", raise_exception=True)
                    def book_list(request):
                        books = Book.objects.all()
                            return render(request, "bookshelf/book_list.html", {"books": books})


                            @permission_required("bookshelf.can_create", raise_exception=True)
                            def book_create(request):
                                if request.method == "POST":
                                        form = BookForm(request.POST)
                                                if form.is_valid():
                                                            form.save()  # ✅ prevents SQL injection, safe ORM usage
                                                                        return redirect("book_list")
                                                                            else:
                                                                                    form = BookForm()
                                                                                        return render(request, "bookshelf/form_example.html", {"form": form})


                                                                                        @permission_required("bookshelf.can_edit", raise_exception=True)
                                                                                        def book_edit(request, pk):
                                                                                            book = get_object_or_404(Book, pk=pk)
                                                                                                if request.method == "POST":
                                                                                                        form = BookForm(request.POST, instance=book)
                                                                                                                if form.is_valid():
                                                                                                                            form.save()
                                                                                                                                        return redirect("book_list")
                                                                                                                                            else:
                                                                                                                                                    form = BookForm(instance=book)
                                                                                                                                                        return render(request, "bookshelf/form_example.html", {"form": form})


                                                                                                                                                        
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
        return render(request, "bookshelf/book_list.html", {"books": books})

        @permission_required("bookshelf.can_create", raise_exception=True)
        def book_create(request):
            if request.method == "POST":
                    title = request.POST.get("title")
                            author = request.POST.get("author")
                                    Book.objects.create(title=title, author=author)
                                            return redirect("book_list")
                                                return render(request, "bookshelf/book_form.html")

                                                @permission_required("bookshelf.can_edit", raise_exception=True)
                                                def book_edit(request, pk):
                                                    book = get_object_or_404(Book, pk=pk)
                                                        if request.method == "POST":
                                                                book.title = request.POST.get("title")
                                                                        book.author = request.POST.get("author")
                                                                                book.save()
                                                                                        return redirect("book_list")
                                                                                            return render(request, "bookshelf/book_form.html", {"book": book})

                                                                                            @permission_required("bookshelf.can_delete", raise_exception=True)
                                                                                            def book_delete(request, pk):
                                                                                                book = get_object_or_404(Book, pk=pk)
                                                                                                    book.delete()
                                                                                                        return redirect("book_list")
                                                                                                        