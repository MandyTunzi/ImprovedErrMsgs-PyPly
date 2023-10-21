# Check Pangram
# This function checks if a given string is a pangram (contains every letter of the alphabet at least once).
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def is_pangram(input_string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz"
    return set(input_string.lower()) >= alphabet


# For getting user input and running the function.
if __name__ == "__main__":
    input_1 = input("Enter a string:\n")
    print(is_pangram(input_1))
