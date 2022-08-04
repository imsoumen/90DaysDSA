"""
Problem Link:
https://www.codingninjas.com/codestudio/problems/pair-sum_697295

Explanation Link:
https://www.codingninjas.com/codestudio/problem-details/pair-sum_697295
"""

# Method1: 
# This solution partially works

# Time Complexity: O(nlogn)
############################

# from os import *
# from sys import *
# from collections import *
# from math import *

# def pairSum(arr, sum):
#     # Write your code here.
#     arr.sort()
    
#     count_list = {}
#     count = 0
#     for i in range(len(arr)):
#         if sum - arr[i] in count_list:
#             count += count_list[sum - arr[i]]
#         if arr[i] in count_list:
#             count_list[arr[i]] += 1
#         else:
#             count_list[arr[i]] = 1

#     strt = 0
#     end = len(arr)-1
#     out = []

#     while strt < end:
#         if arr[strt] + arr[end] < sum:
#             strt += 1
#         elif arr[strt] + arr[end] > sum:
#             end -= 1
#         else:
#             if count_list[arr[strt]] > 1:
#                 for i in range(count_list[arr[strt]]):
#                     out.append([arr[strt],arr[end]])
#             elif count_list[arr[end]] > 1:
#                 for i in range(count_list[arr[end]]):
#                     out.append([arr[strt],arr[end]])
#             else:
#                 out.append([arr[strt],arr[end]])
#             strt += 1
#             end -= 1
#     return out


# Method2: 
# Running through the array

# Time Complexity: O(n^2)
############################

def pairSum(arr, sum):
    # Write your code here.
    arr.sort() 
    out=[]
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==sum:
                out.append([arr[i],arr[j]])
    
    return out




