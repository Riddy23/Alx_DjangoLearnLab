from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Create default groups and assign permissions'

        def handle(self, *args, **options):
                Book = apps.get_model('bookshelf', 'Book')
                        perm_labels = ['can_view', 'can_create', 'can_edit', 'can_delete']
                                perms = {}
                                        for codename in perm_labels:
                                                    try:
                                                                    perms[codename] = Permission.objects.get(content_type__app_label='bookshelf', codename=codename)
                                                                                except Permission.DoesNotExist:
                                                                                                self.stdout.write(self.style.ERROR(f'Permission {codename} not found. Did you run migrations?'))
                                                                                                                return

                                                                                                                        groups_config = {
                                                                                                                                    'Viewers': ['can_view'],
                                                                                                                                                'Editors': ['can_view', 'can_create', 'can_edit'],
                                                                                                                                                            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
                                                                                                                                                                    }

                                                                                                                                                                            for group_name, perm_keys in groups_config.items():
                                                                                                                                                                                        group, created = Group.objects.get_or_create(name=group_name)
                                                                                                                                                                                                    group.permissions.set([perms[k] for k in perm_keys])
                                                                                                                                                                                                                group.save()
                                                                                                                                                                                                                            self.stdout.write(self.style.SUCCESS(f'Group {group_name} created/updated with permissions: {perm_keys}'))

                                                                                                                                                                                                                                    self.stdout.write(self.style.SUCCESS('Groups and permissions configured.'))
                                                                                                                                                                                                                                    