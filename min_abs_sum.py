import time

def solution(A):    
    n = len(A)
    
    if n < 2:
        return 0 if not n else A[0]   
    maximum = 0
    for i in range(n):
        A[i] = abs(A[i])
        maximum += A[i]

    # Array 
    A.sort()

    mid_point = maximum // 2
    A_left = A_right = 0
    O_left = O_right = 0
    for i in range(n-1, -1, -1):       
        if A_right + A[i] <= mid_point and A_right < A_left:
            A_right += A[i]
        else:
            A_left += A[i]        
        if O_right + A[i] <= mid_point or O_right < O_left:
            O_right += A[i]
        else:
            O_left += A[i]        
    return min(abs(A_left - A_right), abs(O_left - O_right))