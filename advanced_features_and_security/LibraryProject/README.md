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
