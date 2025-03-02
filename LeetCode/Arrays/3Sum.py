"""
Problem Link:
https://leetcode.com/problems/3sum/

"""

""" 
Brute Force Method 1: 
Time Complexity: O(N^3)
Space Complexity: O(N)
"""
class Solution:
    def threeSum(self, nums):
        # Create an empty set to store unique triplets
        triplet_set = set()

        n = len(nums)

        # Check all possible triplets
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Found a triplet that sums up to target
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        triplet_set.add(tuple(temp))
        
        # Convert set to list of lists (unique triplets)
        ans = [list(triplet) for triplet in triplet_set]

        return ans


""" 
Better Method 2: 
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    # Function to find triplets having sum equals to 0
    def threeSum(self, nums):
        # Set to store unique triplets
        triplet_set = set()

        n = len(nums)

        # Check all possible triplets
        for i in range(n):
            # Set to store elements seen so far in the loop
            hashset = set()

            for j in range(i + 1, n):
                # Calculate the 3rd element needed to reach target
                third =  - (nums[i] + nums[j])

                """ Find if third element exists in
                 hashset (complements seen so far)"""
                if third in hashset:
                    # Found a triplet that sums up to target
                    temp = [nums[i], nums[j], third]

                    """ Sort the triplet to ensure
                    uniqueness when storing in set"""
                    temp.sort()
                    triplet_set.add(tuple(temp))

                """ Insert the current element 
                into hashset for future checks"""
                hashset.add(nums[j])

        # Convert set to list of lists (unique triplets)
        ans = [list(triplet) for triplet in triplet_set]

        return ans
    
""" 
Optimal Method 2: 
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def threeSum(self, nums):
        
        ans = []
        nums.sort()
        
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0 : j += 1
                elif sum > 0 : k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1

        return ans