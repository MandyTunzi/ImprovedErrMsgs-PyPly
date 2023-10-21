# Word Frequency Counter:
# The following function takes a string and returns a dictionary containing the frequency of each word in the string.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def word_frequency_counter(text):
    text = ''.join(c for c in text if c.isalnum() or c.isspace()).lower()

    words = text.split()

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


# For getting user input and running the function.
if __name__ == '__main__':
    strng = input("Enter a string:\n")
    print(word_frequency_counter(strng))