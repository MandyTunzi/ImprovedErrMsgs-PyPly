# Factorial:
# This function calculates the factorial of a given positive integer.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def factorial(n):
    if n == 0
        return 1
    else:
        return n * factorial(n-1)


# For getting user input and running the function.
if __name__ == "__main__":
    num = int(input("Enter a positive integer:\n"))
    print(factorial(num))
