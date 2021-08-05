"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from itertools import permutations

def no_duplicates_permutation(nums):

    final = []

    perms = permutations(nums)

    for i in perms:
        final.append(i)

    return set(final)

nums = [1, 2, 1]
print(no_duplicates_permutation(nums))