import time
import random

def brute_force_validator(A):
    n = len(A)
    A.sort()
    result = 0
    for z in range(2, n):
        for y in range(1, z):
            for x in range(0, y):
                if A[x]+A[y] > A[z]:
                    result += 1
    return result

def ncr(r, n):
    if r == n:
        return 1
    elif r + 1 == n:
        return n
    elif r > n:
        return 0
    else:
        return r * ncr(r, n-1)

def solution(A):
    n = len(A)
    A.sort()
    result = 0
    for x in range(0, n-2): 
        y = x + 1
        z = x + 2        
        while z<n:
            if A[x] + A[y] > A[z]:
                result += z - y
                z += 1                
            elif y < z - 1:
                y += 1
            else:
                y += 1; z += 1
    return result