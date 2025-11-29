#What are Variables in Python?

"""a variable is essentially a name you give to a location in memory.
    This location holds a value. Think of a variable as a label or a tag 
    that points to a piece of data, not a box that contains the data."""

#Assignment: You create a variable by using the assignment operator (=).

x = 10  # Here, 'x' is a variable that holds the integer value 10
name = "Alice"  # 'name' is a variable that holds the string "Alice"
pi = 3.14  # 'pi' is a variable that holds the float value 3.14


"""Dynamic Typing: Python is dynamically typed. 
    This means you don't have to declare the variable's type 
    (e.g., integer, string) before you use it. 
    Python figures out the type automatically based on the value you assign."""

"""Type Flexibility: A single variable can hold values of different types 
    throughout its lifetime. If you change the value, the variable's 
    type may change as well."""



"""Code        Current Value           Variable Type           Explanation

x           10                      Integer                 Initially holds an integer
x           "Hello"                 String                  Now holds a string
x           3.14                    Float                   Now holds a float"""

"""Variable Naming Rules:
1. Must start with a letter (a-z, A-Z) or an underscore (_).
2. Can contain letters, digits (0-9), and underscores after the first character.
3. Cannot be a reserved keyword in Python (like if, for, while, etc.).
4. Case-sensitive (e.g., myVar and myvar are different variables).
5. Should be descriptive to make the code more readable (e.g., use 'age' instead of 'a').
6. Cannot contain spaces or special characters (like !, @, #, $, %, etc.).
7. variable names meaningful and avoid single-letter names except for counters or iterators."""



age = 25  # Good variable name
Age = 30  # Different variable due to case sensitivity
#1_name = "Bob"  # Invalid: starts with a digit
_1_name = "David"  # Valid: starts with an underscore
first-name = "Charlie"  # Invalid: contains a hyphen



