"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution(object):

    def search_positions(self, nums, target):
        nums_str = ""
        target = str(target)
        for i in nums:
            nums_str += str(i)
        start_pos = nums_str.find(target)
        last_pos = nums_str.rfind(target)
        return [start_pos, last_pos]
        

solution = Solution()
nums = [5,7,7,8,8,10]
target = 6
print(solution.search_positions(nums, target))