from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book


# Forms for CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
            model = CustomUser
                    fields = ("username", "email", "date_of_birth", "profile_photo")


                    class CustomUserChangeForm(UserChangeForm):
                        class Meta:
                                model = CustomUser
                                        fields = ("username", "email", "date_of_birth", "profile_photo")


                                        # Secure form for Book model
                                        class BookForm(forms.ModelForm):
                                            class Meta:
                                                    model = Book
                                                            fields = ["title", "author", "published_date"]

                                                                    # Add basic widgets for better UX & validation
                                                                            widgets = {
                                                                                        "title": forms.TextInput(attrs={"placeholder": "Enter book title"}),
                                                                                                    "author": forms.TextInput(attrs={"placeholder": "Enter author name"}),
                                                                                                                "published_date": forms.DateInput(attrs={"type": "date"}),
                                                                                                                        }
                                                                                                                        