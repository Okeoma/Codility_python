# Best Solution
def solution(A):
# write your code in Python 3.6
    if len(A) < 3:
        return 0
    elif len(A) == 3:
        return A[0]*A[1]*A[2]

    A.sort()
    max_negative_d = A[0] * A[1]
    max_negative_t = A[-1] * A[-2] * A[-3]
    return max(A[-1] * max(A[-2] * A[-3], max_negative_d), max_negative_t) 
    
    
# Solution 2

# A O(n) Python3 program to find maximum
# product pair in an array.
import sys
 
# Function to find a maximum product
# of a triplet in array of integers
# of size n
def maxProduct(arr, n):
 
    # If size is less than 3, no
    # triplet exists
    if (n < 3):
        return -1
 
    # Initialize Maximum, second
    # maximum and third maximum
    # element
    maxA = -sys.maxsize - 1
    maxB = -sys.maxsize - 1
    maxC = -sys.maxsize - 1
 
    # Initialize Minimum and
    # second minimum element
    minA = sys.maxsize
    minB = sys.maxsize
 
    for i in range(n):
 
        # Update Maximum, second
        # maximum and third maximum
        # element
        if (arr[i] > maxA):
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
             
        # Update second maximum and
        # third maximum element
        elif (arr[i] > maxB):
            maxC = maxB
            maxB = arr[i]
             
        # Update third maximum element
        elif (arr[i] > maxC):
            maxC = arr[i]
 
        # Update Minimum and second
        # minimum element
        if (arr[i] < minA):
            minB = minA
            minA = arr[i]
 
        # Update second minimum element
        elif (arr[i] < minB):
            minB = arr[i]
 
    return max(minA * minB * maxA,
               maxA * maxB * maxC)