
---

### **4. delete.md**
```markdown
# Delete the Book Instance

```python
from bookshelf.models import Book

# Get the updated book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()
# Expected Output: (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Expected Output: <QuerySet []>
