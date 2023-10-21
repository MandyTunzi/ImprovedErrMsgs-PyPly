# Reverse String:
# The following function reverses a given string.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def reverse_string(input_string):
    return input_string[::-1]
break


# For getting user input and running the function.
if __name__ == "__main__":
    input_strng = input("Enter a string:\n")
    print(reverse_string(input_strng))
