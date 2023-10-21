# Problem: Sum of Prime Factors
# The following function calculates the sum of prime factors for a given number.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def sum_of_prime_factors(n):
    factor_sum = 0
    i = 2
    while i * i <= n:
        if n % i:
        i += 1
        else:
            n //= i
            factor_sum += i
    if n > 1:
        factor_sum += n
    return factor_sum


# For getting user input and running the function.
if __name__ == "__main__":
    num = int(input("Enter an integer:\n"))
    print(sum_of_prime_factors(num))