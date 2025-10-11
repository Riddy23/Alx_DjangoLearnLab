# django_blog (ALX_DjangoLearnLab)

## Setup
1. Create virtualenv and install Django:
   pip install django

   2. Run initial migrations:
      python manage.py makemigrations
         python manage.py migrate

         3. Create superuser:
            python manage.py createsuperuser

            4. Start server:
               python manage.py runserver

               Visit http://127.0.0.1:8000/

               ## Features
               - User registration, login, logout (Django auth).
               - Profile page (bio + avatar).
               - Create/Read/Update/Delete posts (author only edit/delete).
               - Comments (create/edit/delete by comment author).
               - Tags (comma-separated on post form).
               - Search box (title, content, tags).

               ## File highlights
               - `blog/models.py` — Post, Comment, Tag, Profile models.
               - `blog/forms.py` — ModelForms and auth forms.
               - `blog/views.py` — CBVs for posts & comments, functions for auth/profile.
               - `blog/urls.py` — Routes for blog functionality.
               - `templates/` — base, post list/detail, forms, auth templates.

               ## Notes
               - Optional: use django-taggit for advanced tagging.
               - To store avatars, configure MEDIA_URL and MEDIA_ROOT in settings.

               