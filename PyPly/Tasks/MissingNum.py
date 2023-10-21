# Find Missing Number
# The following function called `find_missing_number` finds the missing number in a sequence of consecutive POSITIVE integers.
# If there is no missing number then it returns the following number in the sequence.

# Submit to the automarker to see input and expected output.
# Find the error in the program.

def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(n)
    missing_number = expected_sum - actual_sum
    return missing_number


# For getting user input and running the function.
if __name__ == '__main__':
    input_string = input("Enter a list of integers:\n")
    input_values = input_string.strip()[1:-1]
    input_values_list = input_values.split(',')
    integer_list = [int(value.strip()) for value in input_values_list]
    print(find_missing_number(integer_list))