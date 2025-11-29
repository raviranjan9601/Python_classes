"""Operators are symbols or keywords that tell a programming language to 
perform specific operations on one or more operands (variables, constants, 
or values). They are the fundamental building blocks for creating expressions 
and carrying out computations, comparisons, and logic in code."""

#Operators are typically grouped by the type of operation they perform:

#1. Arithmetic Operators:

"""Arithmetic operators are the foundation of mathematical calculations 
in programming. They are used to perform the basic mathematical 
operations on numerical operands (variables or values)."""

"""Arithmetic operators are two types

a. binary (requiring two operands) 
b. unary (requiring one operand)"""


#Binary Operators (Require Two Operands)

"""These operators are the most common and require a value on both sides of 
the operator."""

#Definition: They take two operands (inputs).

#Examples:
""" Operator,       Name,           Description,                                                                        "Example (A=10, B=3)",      Result
        (+)           Addition       Adds the two operands.,                                                                  A+B                     13

        (-)           Subtraction    Subtracts the second operand from the first.,                                            A−B                      7

        (*)           Multiplication Multiplies the two operands.,                                                            A∗B                     30
        (/)           Division       Divides the first operand by the second.,                                                A/B                     ∼3.33
        
        (%)           Modulus        Returns the remainder of the division.,                                                  A%B                     1

        (//)          Floor Division (Python/Some Languages) Divides and rounds the result down to the nearest whole number.  A//B                    3
        
        (**)          Exponentiation (Python/Some Languages) Raises the first operand to the power of the second.,            A**B                    1000"""

result = 10 + 5  # 10 and 5 are the two operands

#Unary Operators (Require One Operand)

"""These operators apply to a single value and typically deal with 
    the sign of the number."""

#Definition: They take only one operand.

#Examples:
"""Operator	            Name	            Description	                                Example (A=10)	   Result
    ++                  Increment           Increases the value of the operand by 1.    A++ or ++A          11
    --                  Decrement           Decreases the value of the operand by 1.    A-- or --A          9   
    +                   Unary Plus          Indicates a positive value (usually redundant).  +A             10
    -                   Unary Minus         Negates the value of the operand.             -A                 -10 """
x = 5
y = -x    # - is the unary operator, x is the single operand. y becomes -5
z = +x    # + is the unary operator. z remains 5
#Note: Python does not have ++ or -- operators like some other languages (C, C++, Java).