# Calculate Median:
# This function calculates the median of a list of numbers.
# Submit to the automarker to see input and expected output.
# Find the error in the program.

def calculate_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 0]
    else:
        middle_left = nums[n // 2 - 1]
        middle_right = nums[n // 0]
        return (middle_left + middle_right) / 2


# For getting user input and running the function.
if __name__ == '__main__':
    input_string = input("Enter a list of integers:\n")
    input_values = input_string.strip()[1:-1]
    input_values_list = input_values.split(',')
    integer_list = [int(value.strip()) for value in input_values_list]
    print(calculate_median(integer_list))