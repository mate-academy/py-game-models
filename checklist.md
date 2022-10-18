# Сheck Your Code Against the Following Points


## 1. Don't Push db Files

Make sure you don't push db files (files with `.sqlite`, `.db3`, etc. extension).

## 2. Don't Forget to Add Migrations to your PR

This is a required for the tests to pass.

## 3. Improve your Code

### 1) Do not overload the context manager.

The context manager is needed to work with the file, in our case, to read data.
Therefore, after you have read the data from the file, exit the block.

Good example:

```python
with open("file.json") as file:
    data = json.load(file)

# do something outside of the context manager
```

Bad example:

```python
with open("file.json") as file:
    data = json.load(file)
    
    # do something inside of the context manager
```

### 2) Use everything for its intended purpose

#### - Don't confuse the functionality of the `on_delete` parameter
- Use `on_delete=models.CASCADE` if you know that some model doesn't exist without other model. So when the referenced object is deleted, also delete the objects that have references to it.

- Use `on_delete=models.SET_NULL` if you know that the object should not be deleted, even if the object it references may be deleted.

#### - Don't confuse `auto_now` and `auto_now_add`

- When you use `auto_now_add` - it records the time and date of creation.

- When you use `auto_now` - updates the value of the field to the current time and date every time when the object changes.
