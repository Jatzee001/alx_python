def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("(0 chars long)")
    else:
        for row in matrix:
            if not row:
                print(" - [Got]")
            else:
                for i, num in enumerate(row):
                    if i == len(row) - 1:
                        print("{:d}".format(num))
                    else:
                        print("{:d}".format(num), end=" ")