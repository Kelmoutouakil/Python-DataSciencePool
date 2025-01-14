📖 Piscine: Python for Data Science
---
A curated pool of resources and exercises to help you master Python programming.
---
Welcome to the Python Learning Pool! This repository is designed to help beginners and intermediate learners build their Python skills 
through hands-on practice, guided examples, and projects.
---

## Learning Objectives

By using this pool, you will:
- Understand Python fundamentals, including syntax, variables, and data types.
- Learn to write clean, efficient, and reusable code.
- Gain experience in object-oriented programming (OOP).
- Solve real-world problems using Python.

---
## Getting Started

### Prerequisites:
- Install Python (latest version ): [Download Python](https://www.python.org/downloads/)
- Install a code editor (e.g., [VS Code](https://code.visualstudio.com/)).

---
## Topics Covered
This pool covers the following Python concepts:
## Built-in Data Types:
------------------------
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


### 1-List
---
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
all with different qualities and usage.
List items are ordered, indexed, changeable, and allow duplicate values.

### 2-Tuple
---
Tuple items are ordered, unchangeable, indexed, and allow duplicate values.

### 3-Set Items
---
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

### 4-Python Dictionaries
---
Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

## Object Type && Match  case Statement
------------------------
### Object Type 
---
to print an object 's type in python we use 'type' function ,it 's mostly used for debugging purposes,it can be used with single parameter or 3 like this
Syntax: type(object, bases, dict)
object: Required. If only one parameter is specified, the type() function returns the type of this object
bases : tuple of classes from which the current class derives. Later corresponds to the __bases__ attribute. 
dict : a dictionary that holds the namespaces for the class. Later corresponds to the __dict__ attribute.
Return: returns a new type class or essentially a metaclass.
exemple : x = 10
print(type(x))
### Match case statement:
---
It allows us to perform more expressive and readable conditional checks. Unlike traditional if-elif-else chains, which can become unwieldy with complex conditions, the match-case statement provides a more elegant and flexible solution (like switch case in other language).
### What is NaN?
---
NaN stand for not a number.
It is a special value in floating-point arithmetic that represents undefined or unrepresentable results, such as dividing zero by zero or taking the square root of a negative number.
Exemple
nan_value = float("NaN")
print(nan_value == nan_value)  # Output: False

### Using sys.argv
---
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
One such variable is sys.argv which is a simple list structure. It’s main purpose are:

It is a list of command line arguments.
len(sys.argv) provides the number of command line arguments.
sys.argv[0] is the name of the current Python script. 
 
### string.punctuation in Python

In Python, the string module is a pre-initialized string used as a string constant. One such constant is string.punctuation, which provides a predefined string containing all the characters commonly considered punctuation.
import string

# Check if a character is punctuation
char = "!"
if char in string.punctuation:
    print(f"{char}")

### Pyhton input

Python input() function is used to take user input. By default, it returns the user input in form of a string.

input() Function 
Syntax: 


input(prompt)
prompt [optional]: any string value to display as input message


Ex: input(“What is your name? “)


Returns: Return a string value as input by the user.
### Understanding EOFError

The EOFError is raised in several contexts:

Interactive Input: When using the input() in the script that expects user input but does not receive any.
File Handling: When attempting to read past the end of the file using the methods like readline() or read().
Automated Testing: When scripts or tests are run in the environment where user input is not provided as expected.

### Python Lambda Functions
---
Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

In the example, we defined a lambda function(upper) to convert a string to its upper case using upper().
s1 = 'GeeksforGeeks'
s2 = lambda func: func.upper()
print(s2(s1))
### List Comprehension in Python
---
List comprehension is a way to create lists using a concise syntax. It allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range). This helps us to write cleaner, more readable code compared to traditional looping techniques.

For example, if we have a list of integers and want to create a new list containing the square of each element, we can easily achieve this using list comprehension.
a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)
