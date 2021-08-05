"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

class Solution:

    # this functio is used to convert the number from string to integer using the python inbuilt ord() function
    def convert_str_to_int(self, string):
        # initialize the variable
        num = 0
        for i in string:
            # update the number from str to int using the python inbuilt ord() function
            # ord('1') is 49 so 49-48=1 then multiply with 10 to increment its digit place.
            num = num * 10 + (ord(i) - 48)
        return num
    
    # main function for multiply the two strings
    def multiply_strings(self, string1, string2):

        # invoking the convert_str_to_int function for converting strings to integers
        return str(self.convert_str_to_int(string1) * self.convert_str_to_int(string2))

# assigning the static variables to evaluate program
string1 = "123"
string2 = "10"
# initializing the class instance
solution =  Solution()

# printing the final output
print(type(solution.multiply_strings(string1, string2)))