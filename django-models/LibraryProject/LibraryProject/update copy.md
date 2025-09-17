
---

### **3. update.md**
```markdown
# Update the Book Title

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected Output: <Book: Nineteen Eighty-Four>
