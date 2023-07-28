def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    
    return result

# Test the function
print("Correct output - case: a = 10 / b = 2")
result1 = safe_print_division(10, 2)

print("Correct output - case: a = 10 / b = -2")
result2 = safe_print_division(10, -2)

print("Correct output - case: a = 0 / b = 2")
result3 = safe_print_division(0, 2)

print("Correct output - case: a = 10 / b = 0")
result4 = safe_print_division(10, 0)

print("Correct output - case: a = 0 / b = 0")
result5 = safe_print_division(0, 0)