"""
Problem Link:
https://www.codingninjas.com/codestudio/problems/two-sum_839653

Explanation:
https://www.codingninjas.com/codestudio/problem-details/two-sum_839653

"""

""" Method 1: Hashing Method
Time Complexity: O(N)
Space Complexity: O(N)
"""

def twoSum(arr, target, n):
    # Write your code here.
    dictPair = {}
    out = []
    
    for i in range(n):
        if arr[i] in dictPair:
            dictPair[arr[i]] += 1
        else:
            dictPair[arr[i]] = 1
            
        if target - arr[i] not in dictPair:
            continue
            
        if target - arr[i] == arr[i]:
            
            if dictPair[arr[i]] > 1:
                out.append([arr[i],arr[i]])
                dictPair[arr[i]] -= 2
        
        else:
            if dictPair[arr[i]] > 0 and dictPair[target-arr[i]] > 0:
                out.append([arr[i],target-arr[i]])
                dictPair[arr[i]]-=1
                dictPair[target-arr[i]]-=1
                
    if not out:
       out.append([-1,-1])
        
    return out
    
def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)

""" Method 2: Hashing Method
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

def twoSum(arr, target, n):
    # Write your code here.
    out = []
  
    arr.sort()
    
    start=0
    end=n-1
    
    while start<end:
        if arr[start]+arr[end]==target:
            out.append([arr[start],arr[end]])
            start+=1
            end-=1
        elif arr[start]+arr[end]<target:
            start+=1
        elif arr[start]+arr[end]>target:
            end-=1
    if not out:
        out.append([-1,-1])
    
    return out
    
def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)