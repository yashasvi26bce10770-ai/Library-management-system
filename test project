from library_data import add_book, find_book, delete_book

bid = "T001"

add_book({
"id": bid,
"title": "Test Book",
"author": "Test Author",
"category": "Science",
"year": 2025
})

r1 = find_book(bid)
print("Test 1: Book added and found")
assert r1 is not None
assert r1["title"] == "Test Book"

r2 = delete_book(bid)
print("Test 2: Book deleted")
assert r2 is True

r3 = find_book(bid)
print("Test 3: Deleted book not found")
assert r3 is None

print("\nAll tests passed successfully.")
