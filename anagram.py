"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # create a default dictionary using collections module 
        # defaultdict keys must be immutable and unique
        res = defaultdict(list)

        # looping the  list elements using for loop
        for s in strs:

            # sort the value of the each element using sorted() function
            sorted_values = sorted(s)

            # this assigns values to the key where keys are unique 
            # here the keys are sorted ones but the values are original elements
            res[''.join(sorted_values)].append(s)  
        
        # print the defaultdict values() elements for printing the group anagrams
        print(res.values())

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
solution.groupAnagrams(strs)

print(defaultdict(tuple))


"""
detailed explaination:
_2d_list_value = [] , eg: [[a, b], [c, d]]
for s i strs:
    values = [''.join(sorted(s)), s]
    _2d_list_value.append(values)

result = defaultdict(list)
for k, v in _2d_list_value:
    result[k].append(v)

print(result.values())
"""