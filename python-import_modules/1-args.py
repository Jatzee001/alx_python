import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("Number of argument(s): .")
    else:
        plural = "s" if num_arguments > 1 else ""
        print(f"Number of argument(s): {num_arguments}, followed by argument{plural}:")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()