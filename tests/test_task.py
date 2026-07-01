import pytest
import importlib
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_task():
    """Import task module fresh each time."""
    if "task" in sys.modules:
        del sys.modules["task"]
    return importlib.import_module("task")


def test_file_imports_without_errors():
    """task.py must import without crashing."""
    try:
        get_task()
    except Exception as e:
        pytest.fail(
            f"task.py failed to import with error: {e}\n"
            "Fix any syntax errors or missing variables before running other tests."
        )


def test_task1_age_exists_and_is_int():
    """Task 1: `age` must exist and be an integer."""
    task = get_task()
    assert hasattr(task, "age"), (
        "Variable `age` not found. "
        "Create it with: age = 25  (or any whole number between 16 and 99)"
    )
    assert isinstance(task.age, int), (
        f"Task 1: `age` should be an integer (whole number) but got {type(task.age).__name__}.\n"
        "Example: age = 25"
    )
    assert 16 <= task.age <= 99, (
        f"Task 1: `age` should be between 16 and 99 but got {task.age}."
    )


def test_task2_temperature_exists_and_is_float():
    """Task 2: `temperature` must exist and be a float."""
    task = get_task()
    assert hasattr(task, "temperature"), (
        "Variable `temperature` not found. "
        "Create it with: temperature = 20.5  (or any decimal number)"
    )
    assert isinstance(task.temperature, float), (
        f"Task 2: `temperature` should be a float (decimal number) but got {type(task.temperature).__name__}.\n"
        "Make sure your number has a decimal point, e.g. temperature = 20.5"
    )


def test_task3_name_exists_and_is_string():
    """Task 3: `name` must exist and be a non-empty string."""
    task = get_task()
    assert hasattr(task, "name"), (
        "Variable `name` not found. "
        "Create it with: name = \"Ali\"  (use your own first name)"
    )
    assert isinstance(task.name, str), (
        f"Task 3: `name` should be a string but got {type(task.name).__name__}.\n"
        "Wrap your name in quotes: name = \"Ali\""
    )
    assert len(task.name.strip()) > 0, (
        "Task 3: `name` is an empty string. Set it to your first name."
    )


def test_task4_is_student_is_true():
    """Task 4: `is_student` must exist and be the boolean True."""
    task = get_task()
    assert hasattr(task, "is_student"), (
        "Variable `is_student` not found. "
        "Create it with: is_student = True"
    )
    assert isinstance(task.is_student, bool), (
        f"Task 4: `is_student` should be a boolean but got {type(task.is_student).__name__}.\n"
        "Use True or False without quotes: is_student = True"
    )
    assert task.is_student is True, (
        f"Task 4: `is_student` should be True but got {task.is_student}."
    )


def test_task5_result_is_correct():
    """Task 5: `result` must equal (age * 2) + 10."""
    task = get_task()
    assert hasattr(task, "result"), (
        "Variable `result` not found. "
        "Create it with: result = (age * 2) + 10"
    )
    expected = (task.age * 2) + 10
    assert task.result == expected, (
        f"Task 5: `result` should be {expected} (age {task.age} * 2 + 10) "
        f"but got {task.result}.\n"
        "Make sure you use your `age` variable in the calculation: result = (age * 2) + 10"
    )


def test_task6_greeting_is_correct():
    """Task 6: `greeting` must be 'Hello, ' followed by the name variable."""
    task = get_task()
    assert hasattr(task, "greeting"), (
        "Variable `greeting` not found. "
        "Create it with: greeting = \"Hello, \" + name"
    )
    assert isinstance(task.greeting, str), (
        f"Task 6: `greeting` should be a string but got {type(task.greeting).__name__}."
    )
    expected = "Hello, " + task.name
    assert task.greeting == expected, (
        f"Task 6: expected '{expected}' but got '{task.greeting}'.\n"
        "Use string concatenation: greeting = \"Hello, \" + name"
    )
