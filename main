from library_data import add_book, view_books, find_book, delete_book
from library_display import show_books, show_book
from library_utils import get_book_details

while True:

```
print("\n" + "=" * 50)
print("        LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

print("1. Add Book")
print("2. View Books")
print("3. Search Book")
print("4. Delete Book")
print("5. Exit")

ch = input("\nEnter your choice: ")

if ch == "1":

    bk = get_book_details()

    if bk is None:
        print("\nPlease enter all details correctly.")
    else:
        add_book(bk)
        print("\nBook added successfully.")

elif ch == "2":

    bk = view_books()
    show_books(bk)

elif ch == "3":

    bid = input("\nEnter book ID: ")
    bk = find_book(bid)

    if bk is None:
        print("\nBook not found.")
    else:
        show_book(bk)

elif ch == "4":

    bid = input("\nEnter book ID: ")

    if delete_book(bid):
        print("\nBook deleted successfully.")
    else:
        print("\nBook not found.")

elif ch == "5":

    print("\nThank you for using the system!")
    break

else:

    print("\nInvalid choice. Please enter 1 to 5.")
```
