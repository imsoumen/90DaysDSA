
"""
Problem Link:
https://practice.geeksforgeeks.org/problems/max-min/1

Explanation Link:
https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
"""

""" Method 1: 
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findSum(self,A,N): 
        #code here
        min = A[0]
        max = A[0]
        for num in A:
            if num < min:
                min = num
            elif num > max:
                max = num
        return min + max