def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

# Test the function
result = no_c("Hello, World! How are you?")
print(result)  # Output: Hello, World! How are you?
