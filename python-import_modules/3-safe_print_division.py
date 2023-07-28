#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))

    return result

# Test the function
result1 = safe_print_division(10, 2)
result2 = safe_print_division(5, 0)

print("Returned result1:", result1)
print("Returned result2:", result2)