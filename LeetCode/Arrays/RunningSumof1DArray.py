"""
Problem Link:
https://leetcode.com/problems/running-sum-of-1d-array/


"""

""" Method 1: Using a different array
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            if not out:
                out.append(nums[i])
            else:
                out.append(nums[i] + out[len(out)-1])
        
        return out

""" Method 1: Using the same array
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        return nums