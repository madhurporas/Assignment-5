# Assignment-5
# Task-1

This is a simple Python program that allows users to check a student's marks from a predefined dictionary.  
If the student is not found in the dictionary, the program will display an error message.

## 📌 Features
- Stores student names with their marks using a Python dictionary.
- Takes user input for the student name.
- Uses `try-except` to handle cases where the student is not found.
- Provides clean output for both valid and invalid inputs.

## 📝 Code Example
```python
# Dictionary of student names and marks
dict = {"Alice": 20, "Aayushi": 100, "Madhur": 99}

# Taking input
name = input("Enter student name: ")

try:
    # Printing marks if found
    print(f"{name}'s marks: {dict[name]}")
except KeyError:
    # Handling case when student not in dictionary
    print("Student not found")
```
output:
```
Enter student name: Aayushi
Aayushi's marks: 100
```
```
Enter student name: Rahul
Student not found
```
# Task-2
# List Slicing and Reversing in Python

This program demonstrates:
- Extracting a sublist from a list using slicing.
- Copying the sublist.
- Reversing the copied list.

## 📌 Features
- Takes the first five elements of a list.
- Creates a copy of the extracted list.
- Reverses the copied list without affecting the original.
- Prints both extracted and reversed lists.

## 📝 Code Example
```python
# Original list
l = [1,2,3,4,5,6,7,8,9,10]

# Extracting first five elements
l1 = l[0:5]

# Copying and reversing the extracted list
l2 = l1.copy()
l2.reverse()

# Printing results
print(f"Extracted first five elements:{l1}\nReversed extracted elements:{l2}")
```
Output:
```
Extracted first five elements:[1, 2, 3, 4, 5]
Reversed extracted elements:[5, 4, 3, 2, 1]
```
