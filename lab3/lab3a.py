# Define the function again
def hello():
    print('Hello World')
    print('Inside a Function')

# Call the function and assign its return value to a variable
my_stuff = hello()
print('Stuff returned from hello():', my_stuff)
print('The object my_stuff is of type:', type(my_stuff))

# Create a list and use built-in functions and methods
my_list = [3, 6, 2, 8, 4]

# Get the length of the list
print('Length of list:', len(my_list))

# Get the maximum value in the list
print('Max value in list:', max(my_list))

# Append a new value to the list
my_list.append(10)
print('List after append:', my_list)

# Sort the list
my_list.sort()
print('Sorted list:', my_list)
# Looping through the list
for item in my_list:
    print(f'Item: {item}')
import os
os.system('echo "Hello from the OS module"')
import subprocess
subprocess.Popen(['echo', 'Hello from subprocess'])
