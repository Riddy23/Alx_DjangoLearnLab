# advanced_features_and_security/bookshelf/models.py
from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]

def __str__(self):
    return self.title
