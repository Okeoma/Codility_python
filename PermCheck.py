    
# Solution 1
def solution(A)
    A = sorted(A)
    for i in range(0, len(A)):
        if (A[i] != i + 1): 
            return 0 #isn't a number for this position  
    return 1


