"""
Problem Link:
https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1

Explanation Link:
https://www.geeksforgeeks.org/array-rotation/
"""

""" Method 1: Breaking into Temp Array and append the tmp array to the last
Time Complexity: O(N)
Space Complexity: O(N)
"""
# import array
# from math import gcd

# def rotateArr(arr,d):
#     tmp = arr[:d]
#     tmp = arr[d:]+tmp
#     arr = tmp
#     return arr

# if __name__ == '__main__':
#     arr = [1,4,2,5,6,7]
#     d = 3

#     arr = rotateArr(arr,d)

#     for i in arr:
#         print(i,end=' ')


""" Method 2: Move the element one by one
Time Complexity: O(N*d)
Space Complexity: O(1)
"""

# def rotateArr(arr,d):
#     i = 1
#     while(i<=d):
#         last = arr[0]
#         arr.pop(0)
#         arr.append(last)
#         i += 1
#     return arr

# if __name__ == '__main__':
#     arr = [1,4,2,5,6,7]
#     d = 3

#     arr = rotateArr(arr,d)

#     for i in arr:
#         print(i,end=' ')

""" Method 3: Juggling Algorithm
Time Complexity: O(N*d)
Space Complexity: O(1)
"""

def rotateArr(arr,d):
    i = 1
    while(i<=d):
        last = arr[0]
        arr.pop(0)
        arr.append(last)
        i += 1
    return arr

if __name__ == '__main__':
    arr = [1,4,2,5,6,7]
    d = 3

    arr = rotateArr(arr,d)

    for i in arr:
        print(i,end=' ')