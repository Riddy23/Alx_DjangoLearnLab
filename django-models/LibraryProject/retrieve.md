
---

### **2. retrieve.md**
```markdown
# Retrieve the Created Book

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books
# Expected Output: <QuerySet [<Book: 1984>]>

# Access attributes of the first book
book = books.first()
book.title
# Expected Output: '1984'
book.author
# Expected Output: 'George Orwell'
book.publication_year
# Expected Output: 1949
