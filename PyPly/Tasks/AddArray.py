# AddArray:
# This is a function takes an array of integers as input and calculates the sum of all the integer values in the array.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def add_array(arr):
    total = 0
    for num in arr:
        if isinstance(num, int):
            total += num
    return total


# For getting user input and running the function.
if __name__ == '__main__':
    input_string = input("Enter a list of integers:\n")
    input_values = input_string.strip()[1:-1]
    input_values_list = input_values.split(',')
    integer_list = [int(value.strip()) for value in input_values_list]
    print(add_array(integer_list))