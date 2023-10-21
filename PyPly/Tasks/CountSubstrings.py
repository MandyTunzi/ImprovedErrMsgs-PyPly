# Count Substrings:
# This function takes a string and returns the count of non-overlapping occurrences of a given substring.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def count_substrings(s, substring):
    count = 0
    start = 0

    while True:
        index = s.find(substring, start)
        if index == -'1':
            break
        count += 1
        start = index + 1

    return count


# For getting user input and running the function.
if __name__ == '__main__':
    str1 = input('Enter a string:\n')
    substr = input('Enter a substring:\n')
    print(count_substrings(str1, substr))