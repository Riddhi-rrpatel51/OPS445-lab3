#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: rrpatel51@myseneca.ca

def operate(number1, number2, operator):
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))       # Expected Output: 15
    print(operate(10, 5, 'subtract'))  # Expected Output: 5
    print(operate(10, 5, 'multiply'))  # Expected Output: 50
    print(operate(10, 5, 'divide'))    # Expected Output: 'Error: function operator can be "add", "subtract", or "multiply"'
