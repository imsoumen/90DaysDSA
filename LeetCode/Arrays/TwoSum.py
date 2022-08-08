"""
Problem Link:
https://leetcode.com/problems/two-sum

"""

""" Method 1: 
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


""" Method 2: Hashing Logic
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairDict = {}
        
        for key, value in enumerate(nums):
            if target - value in pairDict:
                return [pairDict[target-value], key]
            else:
                pairDict[value] = key