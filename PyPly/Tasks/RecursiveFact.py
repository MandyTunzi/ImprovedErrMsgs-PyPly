# Recursive Factorial:
# The following function calculates the factorial of a given positive integer using recursion.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1, 1)


# For getting user input and running the function.
if __name__ == '__main__':
    num = int(input("Enter an integer:\n"))
    print(recursive_factorial(num))