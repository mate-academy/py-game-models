# Сheck Your Code Against the Following Points


## 1. Don't Push db Files

Make sure you don't push db files (files with `.sqlite`, `.db3`, etc. extension).

## 2. Don't Forget to Add Migrations to your PR

This is a required for the tests to pass. You need to recreate migrations after changes in models.

## 3. Do not forget to add `related_name` to ForeignKey fields

It will allow you to have access to related models on Many side.

## 4. Don't duplicate yourself

**Good example:**

```python
additional_data = data["info"] if data["info"] else None
Model.objects.create(
    field=additional_data
)
```

**Good example and it works well:**

```python
Model.objects.create(
    field=(data["info"] if data["info"] else None)
)
```

**Bad example, avoid using it:**
```python
Model.objects.create(
    field=None
) if data["info"] is None else Model.objects.create(
    field=data["info"]
)
```

## 5. Use `.get()` method to check whether key defined in dictionary

Good example (`.get()` method returns `None` by default):
```python
guild = data.get("guild")
if guild:
    ...
```

Bad example:
```python
if "guild" in data:
    guild = data["guild"]
```

## 6. Improve your Code

### 1) Do not overload the context manager.

The context manager is needed to work with the file, in our case, to read data.
To read a file, you should use the logic within the context manager block only (e.g., `json.load()`).
After finishing this block, you can continue working with the received data.

Good example:

```python
with open("file.json") as file:
    data = json.load(file)
    
player = data["player"]
```

Bad example:

```python
with open("file.json") as file:
    data = json.load(file)
    player = data["player"]
```

### 2) Use everything for its intended purpose

#### - Don't confuse the functionality of the `on_delete` parameter
- Use `on_delete=models.CASCADE` if you know that some model doesn't exist without other model. So when the referenced object is deleted, also delete the objects that have references to it.

- Use `on_delete=models.SET_NULL` if you know that the object should not be deleted, even if the object it references may be deleted.

#### - Don't confuse `auto_now` and `auto_now_add`

- When you use `auto_now_add` - it records the time and date of creation.

- When you use `auto_now` - updates the value of the field to the current time and date every time when the object changes.
