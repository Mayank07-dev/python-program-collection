"""Structure-to-Dictionary conversion.

Shows how to turn common Python structures into dictionaries:
1. list of tuples          -> dict
2. two lists (keys, values) -> dict
3. class object            -> dict
4. dataclass               -> dict
5. nested structure        -> nested dict
"""
from dataclasses import dataclass, asdict


# 1. List of tuples -> dictionary
def tuples_to_dict(pairs):
    return dict(pairs)


# 2. Two lists -> dictionary
def lists_to_dict(keys, values):
    return dict(zip(keys, values))


# 3. Class object -> dictionary
class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch


def object_to_dict(obj):
    return vars(obj)


# 4. Dataclass -> dictionary
@dataclass
class Book:
    title: str
    author: str
    pages: int


# 5. Nested structure -> nested dictionary (recursive)
def to_dict(data):
    if isinstance(data, dict):
        return {k: to_dict(v) for k, v in data.items()}
    if isinstance(data, (list, tuple, set)):
        return [to_dict(item) for item in data]
    if hasattr(data, "__dict__"):
        return {k: to_dict(v) for k, v in vars(data).items()}
    return data


if __name__ == "__main__":
    print("1.", tuples_to_dict([("a", 1), ("b", 2)]))
    print("2.", lists_to_dict(["name", "age"], ["Mayank", 19]))

    s = Student("Mayank", 101, "CSE")
    print("3.", object_to_dict(s))

    b = Book("Clean Code", "Robert Martin", 464)
    print("4.", asdict(b))

    nested = {"student": s, "books": [b, Book("Python Basics", "Anon", 200)]}
    print("5.", to_dict(nested))
