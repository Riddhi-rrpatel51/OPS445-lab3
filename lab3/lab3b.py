#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: rrpatel51@myseneca.ca
def sum_numbers(number1, number2):
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    return number1 - number2

def multiply_numbers(number1, number2):
    return number1 * number2
if __name__ == '__main__':
    print(sum_numbers(10, 5))       # Expected Output: 15
    print(subtract_numbers(10, 5))  # Expected Output: 5
    print(multiply_numbers(10, 5))  # Expected Output: 50
