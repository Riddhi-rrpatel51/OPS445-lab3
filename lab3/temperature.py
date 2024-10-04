def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'

# Test the function
if __name__ == '__main__':
    print(describe_temperature(50))   # Expected: 'hot'
    print(describe_temperature(20))    # Expected: 'perfect'
    print(describe_temperature(-50))   # Expected: 'cold'
    print(describe_temperature(25))    # Expected: 'ok'
    print(describe_temperature(10))    # Expected: 'ok'
