# Fibonacci Sequence:
# Write a function that generates the Fibonacci sequence (where each term in the list represents the sum of the two sums before it)
# up to a given number of terms. Implement recursively.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def fibonacci_recursive_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci_recursive_list(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-3])
        return fib_list


# For getting user input and running the function.
if __name__ == '__main__':
        terms = int(input("Enter an integer for required number of terms in the sequence:\n"))
        print(fibonacci_recursive_list(terms))
