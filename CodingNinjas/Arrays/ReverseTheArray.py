"""
Problem Link:
https://www.codingninjas.com/codestudio/problems/reverse-the-array_1262298

Explanation Link:
https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
"""

#Method 1: Slicing Method
def reverseArray(arr, m):
    # Write your code here.
    req = [i for i in arr[m+1:len(arr)]]
    return arr[0:m+1] + req[::-1]


#Method 2: Running through the array
def reverseArray(arr, m):
    # Write your code here.
    start = m+1
    end = len(arr)-1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1

    return arr

