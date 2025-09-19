from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Set up default groups and assign permissions"

        def handle(self, *args, **kwargs):
                permissions = {
                            "Viewers": ["can_view"],
                                        "Editors": ["can_view", "can_create", "can_edit"],
                                                    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
                                                            }

                                                                    for group_name, perms in permissions.items():
                                                                                group, created = Group.objects.get_or_create(name=group_name)
                                                                                            for perm in perms:
                                                                                                            permission = Permission.objects.get(codename=perm, content_type__app_label="bookshelf")
                                                                                                                            group.permissions.add(permission)
                                                                                                                                        self.stdout.write(self.style.SUCCESS(f"Group {group_name} set up with permissions"))
                                                                                                                                        