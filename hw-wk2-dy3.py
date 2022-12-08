# Exercise 1
# Given an array of positive integers 'nums', return a list of all of the negative integers.
# Example:
# nums = [1, 3, 5, 8, 9]
# Expected Output: [-1, -3, -5, -8, -9]

def turn_negative(nums):
    nums = [num * -1 for num in nums]
    return nums

negative_nums = [4, 123, 88, 53, 11, 2, 94]
print(turn_negative(negative_nums))


# Exercise 2
# Given a string, return a list of all of the digits in the string
# Example:
# address = "123 Real Street, Apt 2, Springfield OR 43498"
# Expected Output: ['1','2','3','2','4','3','4','9','8']
# Hint: Look at string methods.

def find_digits(address_string):
    address_string = [c for c in address_string if c.isdigit()]
    return address_string

address = "1537 South Holt Ave, Los Angeles CA, 90035"
print(find_digits(address))

# Exercise 3
# Given a string 'digits', return a string of the digits +1
# Example:
# digits = '123'
# Output: '124'

def add_by_one(digits):
    return str(int(digits) + 1)

my_string = '25'
print(add_by_one(my_string))