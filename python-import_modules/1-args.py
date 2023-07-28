import sys

num_arguments = len(sys.argv) - 1

if num_arguments == 0:
    print("0 arguments.")
elif num_arguments == 1:
    print("1 argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{num_arguments} arguments:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")