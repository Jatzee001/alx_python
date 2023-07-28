import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("Number of argument(s): .")
    elif num_arguments == 1:
        print("Number of argument(s): 1, followed by argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"Number of argument(s): {num_arguments}, followed by arguments:")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")