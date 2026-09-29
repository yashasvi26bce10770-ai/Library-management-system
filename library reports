def show_summary(bk):
print("\n" + "=" * 50)
print("              LIBRARY SUMMARY")
print("=" * 50)

```
if len(bk) == 0:
    print("No books available.")
    return

print("Total Books:", len(bk))

categories = []

for b in bk:
    if b["category"] not in categories:
        categories.append(b["category"])

print("Categories:", len(categories))

for c in categories:
    count = 0

    for b in bk:
        if b["category"] == c:
            count += 1

    print(c + ":", count)
```
