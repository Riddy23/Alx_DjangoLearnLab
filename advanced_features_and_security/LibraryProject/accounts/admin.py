from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
                                                                                                

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_staff", "profile_preview")
    search_fields = ("username", "email", "first_name", "last_name")

    def profile_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.profile_photo.url)
        return "—"

    profile_preview.short_description = "Profile"
                                                                                