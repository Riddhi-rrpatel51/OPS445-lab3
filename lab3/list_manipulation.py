#!/usr/bin/env python3

# Initial list of courses
courses = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# Print the first course
print(courses[0])  # Output: 'uli101'

# Change the first course
courses[0] = 'eac150'
print(courses[0])  # Output: 'eac150'
print(courses)     # Output: ['eac150', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# Use built-in methods to manipulate the list
courses.append('ops235')    # Add a new item to the end of the list
print(courses)              # Output: ['eac150', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635', 'ops235']

courses.insert(0, 'hwd101') # Insert 'hwd101' at the beginning
print(courses)              # Output: ['hwd101', 'eac150', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635', 'ops235']

courses.remove('ops335')    # Remove the first occurrence of 'ops335'
print(courses)              # Output: ['hwd101', 'eac150', 'ops235', 'ops445', 'ops535', 'ops635', 'ops235']

# Copy and sort the list
sorted_courses = courses.copy() # Create a copy of the courses list
sorted_courses.sort()           # Sort the new list 
print(courses)                  # Output: Original courses list after modifications
print(sorted_courses)           # Output: Sorted list of courses

# Working with a list of numbers
list_of_numbers = [1, 5, 2, 6, 8, 5, 10, 2]
length_of_list = len(list_of_numbers)    # Length of the list
smallest_in_list = min(list_of_numbers)  # Smallest value in the list
largest_in_list = max(list_of_numbers)   # Largest value in the list

print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))
