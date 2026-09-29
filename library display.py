def show_books(bk):
print("\n" + "=" * 60)
print("                 LIBRARY BOOKS")
print("=" * 60)

```
if len(bk) == 0:
    print("No books found.")
    return

for b in bk:
    print("ID:", b["id"])
    print("Title:", b["title"])
    print("Author:", b["author"])
    print("Category:", b["category"])
    print("Year:", b["year"])
    print("-" * 60)
```

def show_book(bk):
print("\n" + "=" * 50)
print("              BOOK DETAILS")
print("=" * 50)
print("ID:", bk["id"])
print("Title:", bk["title"])
print("Author:", bk["author"])
print("Category:", bk["category"])
print("Year:", bk["year"])
