# Permissions and Groups Setup

## Custom Permissions
Defined in `bookshelf/models.py` under the `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Defined via management command `setup_groups`:
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Views
Protected with `@permission_required`:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`

## How to Test
1. Run `python manage.py setup_groups`.
2. Create test users in admin.
3. Assign them to groups.
4. Login as each user and verify permissions.


# Django Security Best Practices

## 1. Secure Settings
- `DEBUG = False` in production
- `SECURE_BROWSER_XSS_FILTER = True` (XSS protection)
- `SECURE_CONTENT_TYPE_NOSNIFF = True` (MIME sniffing prevention)
- `X_FRAME_OPTIONS = 'DENY'` (clickjacking protection)
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` (HTTPS-only cookies)

## 2. CSRF Protection
- All forms include `{% csrf_token %}` in templates.

## 3. SQL Injection Prevention
- Always use Django ORM (`.save()`, `.filter()`, `.get()`) instead of raw SQL.
- User input is validated with Django Forms.

## 4. Content Security Policy (CSP)
- Implemented using `django-csp` middleware.
- Restricts scripts, styles, and fonts to trusted domains.

## 5. Testing
- Verified CSRF tokens included in forms.
- Checked forms against XSS by submitting malicious scripts.
- Confirmed users without permissions cannot access restricted views.


