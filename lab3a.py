# Function that returns a greeting string
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting
# Calling the return_text_value function and assigning the result
text = return_text_value()
print(text)
# Function that returns an integer value
def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3
# Calling the return_number_value function
number = return_number_value()
print(number)          # Should print 15
print(number + 5)      # Should print 20
print(return_number_value() + 10)  # Should print 25
# Attempt to combine a string and a number (will produce an error)
number = return_number_value()
try:
    print('my number is ' + number)  # This will raise an error
except TypeError as e:
    print(f'Error: {e}')
# Correctly combining a string and a number by converting the number to a string
print('my number is ', number)                   # Using comma to separate values
print('my number is ' + str(number))             # Using str() to convert the number
print('my number is ' + str(return_number_value()))  # Directly convert the returned value
