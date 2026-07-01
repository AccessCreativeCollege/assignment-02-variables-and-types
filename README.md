# Assignment 2: Variables and Data Types

Practice declaring variables of different types and performing basic arithmetic
and string operations.

## Your tasks

Open `task.py` and complete each TODO. **Do not change the variable names** -
the tests look for specific names.

| Task | Variable | What to do |
|------|----------|-----------|
| 1 | `age` | Set to any whole number between 16 and 99 |
| 2 | `temperature` | Set to any decimal number |
| 3 | `name` | Set to your first name as a string |
| 4 | `is_student` | Set to the boolean `True` |
| 5 | `result` | Set to `(age * 2) + 10` using your `age` variable |
| 6 | `greeting` | Combine `"Hello, "` with your `name` variable |

## Data types recap

```python
age = 25            # int - whole number, no decimal point
temperature = 20.5  # float - decimal number
name = "Ali"        # str - text, always in quotes
is_student = True   # bool - either True or False (capital letter, no quotes)
```

## Running the tests yourself

```
pytest tests/ -v
```

## Submitting

```
git add .
git commit -m "Completed assignment 2"
git push
```
