import json

FN = "books.json"

def view_books():
try:
fl = open(FN, "r")
bk = json.load(fl)
fl.close()
return bk
except FileNotFoundError:
return []

def add_book(bk):
dt = view_books()
dt.append(bk)

```
fl = open(FN, "w")
json.dump(dt, fl, indent=4)
fl.close()
```

def find_book(bid):
dt = view_books()

```
for bk in dt:
    if bk["id"] == bid:
        return bk

return None
```

def delete_book(bid):
dt = view_books()
new_dt = []
found = False

```
for bk in dt:
    if bk["id"] == bid:
        found = True
    else:
        new_dt.append(bk)

fl = open(FN, "w")
json.dump(new_dt, fl, indent=4)
fl.close()

return found
```
