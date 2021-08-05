""""
Given an array of integers nums and an integer target
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution.
you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

eg:

9 - 2 = 7
9 - 7 = 2

1 + 3 = 2
1 + 2 = 3
"""


def addsum(nums, target):

    # define a dict which is used to store the nums and indexes
    dict = {}

    # use enumerate methods for getting the index and values of the list(nums)
    for index, number in enumerate(nums):

        # now subtract the number from target -> gives add of two numbers
        num = target - number

        # for sub of two numbers use the
        # num = target + number

        # check if the number is present in the dictionary or not
        # num always check the key
        if num in dict:
            # if it is present in the dict return that number
            # with number as key and index as value
            return [dict[num], index]

        # if num is not present in the dictionary save to the dict object
        dict[number] = index

    # return an empty list if end result not matches
    return []


nums = [3, 2, 4]
target = 5
print(addsum(nums, target))
