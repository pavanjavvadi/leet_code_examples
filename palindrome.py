"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121.
From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # store x val in temp var
    temp = x

    # use pal_of_x for palindrome value
    pal_of_x = 0

    # repeat the loop until x > 0. check each time whether x is > 0 or not
    while x > 0:
        # find the remainder values using modulus
        rem = x % 10

        # creating palindrome value by using the digit position
        pal_of_x = pal_of_x*10 + rem

        # divide the x val for receducig it unit position
        x = x // 10

    # check whether x and output are same or not if same it is palindrome
    if pal_of_x == temp:
        return True

    # if the values are different or x is < o then it return False
    return False


x = int(input("enter your number: "))
print(isPalindrome(x))
