from django.contrib import admin
from .models import Book, Library, Librarian, UserProfile

# Customize Book admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
        search_fields = ("title", "author")
            list_filter = ("publication_year",)

            # Customize Library admin
            @admin.register(Library)
            class LibraryAdmin(admin.ModelAdmin):
                list_display = ("name", "location")
                    search_fields = ("name",)

                    # Customize Librarian admin
                    @admin.register(Librarian)
                    class LibrarianAdmin(admin.ModelAdmin):
                        list_display = ("first_name", "last_name", "email")
                            search_fields = ("first_name", "last_name", "email")

                            # Customize UserProfile admin
                            @admin.register(UserProfile)
                            class UserProfileAdmin(admin.ModelAdmin):
                                list_display = ("user", "role")
                                    list_filter = ("role",)
                                        search_fields = ("user__username",)
                                        