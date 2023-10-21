# FizzBuzz:
# This function shows the classic fibonacci problem that:
# Prints numbers from 1 to imput integer,
# but for multiples of 3, prints "Fizz" instead of the number,
# and for multiples of 5, prints "Buzz."
# For numbers that are multiples of both 3 and 5, prints "FizzBuzz."

# Submit to the automarker to see input and expected output.
# Find the error in the program.

def fizzbuzz(num):
    result = []
    for num in range(1, num + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 = 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result
    

# For getting user input and running the function.
if __name__ == "__main__":
    num = int(input("Enter an integer:\n"))
    print(fizzbuzz(num))
