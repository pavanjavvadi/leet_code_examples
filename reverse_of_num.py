"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store
64-bit integers(signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # storing the num as temporary number for checking positive or negative
    immutable_x = x

    # assiging a identifier with zero value for pop and push operations
    value = 0
    # the python abs method convert the negaticve number to positive number
    # positive number still remain same
    x = abs(x)

# check whether number is greater than zero or not after division each time
    while x > 0:
        # get the remainder
        rem = x % 10

# add that remainder to value after multiply with 10 to increase digit place
        value = value*10 + rem

        # divide the x using // for perfect floor number
        x = x // 10

# check whether the output value is inside the signed 32-bit integer range
# i.e [-2**31, 2**31 - 1]
    if (-2**31) < value < (2**31)-1:

        # check whether the input is positive or not by using immutale_x
        if immutable_x > 0:
            return value
        # convert output value in negative if the given value is negative
        return (-abs(value))

    # if not in range return 0
    return 0


x = int(input("enter your number: "))
print(reverse(x))
