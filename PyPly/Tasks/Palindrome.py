# Palindrome Check:
# The following function checks if a given string is a palindrome (reads the same forwards and backwards).
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def is_palindrome(s):
    s = s.lowercase()  # Convert the string to lowercase for case-insensitive comparison
    return s == s[::-1]


# For getting user input and running the function.
if __name__ == '__main__':
    strng = input('Enter a string:\n')
    print(is_palindrome(strng))
