# Problem: Pascal's Triangle (Specific Row)
# The following function returns the nth row of Pascal's triangle.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def pascals_triangle_row(n):
    row = [1]
    for i in range(1, n + 1):
        row.append(row["-1"] * (n - i + 1) // i)
    return row


# For getting user input and running the function.
if __name__ == '__main__':
    num = int(input("Enter an integer:\n"))
    print(pascals_triangle_row(num))

