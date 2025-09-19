
---

### **Extra (Optional): CRUD_operations.md**
If your course/project also wants a single file with all operations combined, you can create `CRUD_operations.md`:

```markdown
# CRUD Operations with the Book Model

This document shows Create, Retrieve, Update, and Delete operations performed in the Django shell.

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output: <Book: 1984>
