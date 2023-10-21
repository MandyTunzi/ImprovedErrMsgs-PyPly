# Find Minimum and Maximum:
# This funtion takes a list of numbers and returns the minimum and maximum values in the list.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def find_min_max(numbers):
    if not numbers:
        return None, None  # If the list is empty, return None for both min and max

    min_val = max_val

    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val


# For getting user input and running the function.
if __name__ == '__main__':
    input_string = input("Enter a list of integers:\n")
    input_values = input_string.strip()[1:-1]
    input_values_list = input_values.split(',')
    integer_list = [int(value.strip()) for value in input_values_list]
    print(find_min_max(integer_list))