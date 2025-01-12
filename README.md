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

<<<<<<< HEAD
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

=======
## Dates && Times in Python:
------------------------
### Python datetime
---
In Python, date and time are not data types of their own, but a module named DateTime in Python can be imported to work with the date as well as time. Python Datetime module comes built into Python, so there is no need to install it externally. 
Python Datetime module supplies classes to work with date and time. These classes provide several functions to deal with dates, times, and time intervals. Date and DateTime are an object in Python, so when you manipulate them, you are manipulating objects and not strings or timestamps. 

The DateTime module is categorized into 6 main classes – 

date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month, and day. you can refer to – Python DateTime – Date Class
time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo. You can refer to – Python DateTime – Time Class
date-time – It is a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo. You can refer to – Python DateTime – DateTime Class
timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution. You can refer to – [Python DateTime – Timedelta Class](https://www.geeksforgeeks.org/python-datetime-tzinfo/)
tzinfo – It provides time zone information objects. You can refer to – Python – datetime.tzinfo()
timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2). You can refer to –[ Handling timezone in Python](https://www.geeksforgeeks.org/handling-timezone-in-python/)
>>>>>>> b8692560e115f1f7d1ed906285cf1ac14bc489e1




