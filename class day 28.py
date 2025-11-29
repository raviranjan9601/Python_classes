#Python Dictionary

"""A dictionary in Python is a built-in, unordered, and mutable data structure 
    used to store collections of data. It holds data in key-value pairs."""

#Key Features of Python Dictionaries

"""Unordered: The items in a dictionary do not have a defined order, and
    the order may change when new items are added.  """

"""Mutable (Changeable): You can add, remove, and modify items after the dictionary 
    has been created."""

"""Indexed: Dictionaries are indexed by their keys, not by a range of numbers."""

"""No Duplicates: A dictionary cannot have two items with the same key. 
    If you try to insert an item with a key that already exists, the 
    new value will overwrite the old value."""

#Structure and Syntax

"""Dictionaries are created using curly braces ({}), with keys and values 
    separated by a colon(:). The pairs are separated by commas."""

#Syntax:

my_dictionary = {
                "key1": "value1", 
                "key2": "value2",
                "key3": "value3"}

#Example:
student_info = {
    "name": "Ravi",
    "age": 20,
    "Subject": "Computer Science",
    "is_active": True

}

#Key and Value Rules
    #Keys
"""Keys Must be unique."""
"""Must be immutable data types (e.g., strings, numbers (integers, floats), 
    and tuples). Lists and other dictionaries cannot be used as keys."""

#Values
"""Values Can be any data type (string, number, list, tuple, another dictionary, 
    function, etc.)."""
"""Values Can be duplicates (multiple keys can point to the same value)."""

#Common Dictionary Operations

#1. Accessing Items

"""You access the value of an item by referring to its key inside square brackets 
or by using the .get() method."""

# Using square brackets
name = student_info["name"]  # Output: 'Ravi'

# Using the .get() method (safer, returns None if key is not found)
age = student_info.get("age")  # Output: 20

#2. Adding or Modifying Items

"""To add a new item or change an existing one, you assign a value to a key."""

# Adding a new item
student_info["city"] = "Patna"
# student_info is now: {'name': 'Ravi', 'age': 20, 'Subject': 'Computer Science', 'is_active': True, 'city': 'Patna'}

# Modifying an existing item
student_info["age"] = 21
# student_info is now: {'name': 'Ravi', 'age': 21, ...}

#3. Removing Items

"""You can use the del keyword or methods like .pop() or .clear()."""

# Using del keyword
del student_info["city"]

# Using .pop() (removes the item with the specified key and returns the value)
Subject = student_info.pop("Subject")  # Subject is 'Computer Science', item is removed

# Using .clear() (removes all items)
# student_info.clear()  # student_info becomes {}

#4. Looping Through a Dictionary

"""You can iterate through the dictionary's keys, values, or key-value pairs."""

#Method         What it Returns
""" for k in dict:  Keys (default)
    dict.keys()     A view object of all keys
    dict.values()   A view object of all values
    dict.items()    A view object of key-value pairs (as tuples)"""

# Looping through key-value pairs
for key, value in student_info.items():
    print(f"{key}: {value}")


#The .update() Method

"""The .update() method is used to add items from one dictionary 
    (or any iterable of key-value pairs) to another dictionary. 
    It's especially useful for combining data or applying patch updates."""

#1. Adding/Merging Items

"""If the key from the source dictionary does not exist in the target dictionary, 
    the new key-value pair is simply added."""

# Target dictionary
user_data = {"id": 101, "name": "Ravi Kr.", "city": "Beguasari"}

# Source dictionary with new data
new_info = {"country": "IND", "status": "active"}

user_data.update(new_info)

# Result: {'id': 101, 'name': 'Alex', 'city': 'London', 'country': 'UK', 'status': 'active'}
print(user_data)


#2. Overwriting Existing Values

"""If the key from the source dictionary already exists in the target dictionary, 
    its value is overwritten with the new value from the source."""

# Target dictionary
item_prices = {"apple": 50, "banana": 30}

# Source dictionary with price changes
price_update = {"apple": 60, "orange": 75}

item_prices.update(price_update)

# Result: 'apple' value is updated, 'orange' is added
# {'apple': 60, 'banana': 30, 'orange': 75}
print(item_prices)

#Dictionary Comprehensions

"""A Dictionary Comprehension provides a concise, single-line way to create a 
    dictionary. It follows a similar structure to list comprehensions and is 
    often much more efficient and readable than using a for loop to build a 
    dictionary item by item."""

#Syntax

#The general syntax is:
"{key_expression: value_expression for item in iterable if condition}"


#Examples

#1. Squaring Numbers

"""Create a dictionary where the keys are numbers and the values are their 
squares."""

numbers = [1, 2, 3, 4, 5]

squared_dict = {num: num ** 2 for num in numbers}

# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squared_dict)

#2. Conditional Filtering

"""Only include items where a condition is met 
(e.g., key length is greater than 5)."""

original_dict = {"apple": 5, "banana": 6, "kiwi": 2, "grape": 4}

long_keys_dict = {k: v for k, v in original_dict.items() if len(k) > 5}

# Result: {'banana': 6}
print(long_keys_dict)

#3. Swapping Keys and Values

"""You can quickly swap the keys and values, provided the values are unique 
(since the new keys must be unique)."""

code_names = {"USA": "Dollars", "JPN": "Yen", "EUR": "Euro"}

# Swap keys and values
names_code = {v: k for k, v in code_names.items()}

# Result: {'Dollars': 'USA', 'Yen': 'JPN', 'Euro': 'EUR'}
print(names_code)


