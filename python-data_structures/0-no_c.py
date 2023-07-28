def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

# Test cases
test_cases = [
    "School",
    "Chicago",
    "Holberton",
    "Holberton School",
    "",
    "HellcCcccooccoscccss",
]

for word in test_cases:
    print(f"Correct output - case: word = \"{word}\"")
    result = no_c(word)
    print(result)
    print()
