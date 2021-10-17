# Python3 program to print largest contiguous array sum

#Correct Solution
from sys import maxsize
 
# Function to find the maximum contiguous subarray
# and print its sum
def solution(A):
    # write your code in Python 3.6
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(0,len(A)): 
        max_ending_here += A[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
 
    return max_so_far

 
from sys import maxsize
 
# Function to find the maximum contiguous subarray
# and print its starting and end index
def solution(A): 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0, len(A)): 
        max_ending_here += A[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
 
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
 
    return (end - start + 1)
 
# Driver program to test solution
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(solution(a,len(a)))
 