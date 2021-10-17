def solution(A):    
    n = len(A)

    if n == 1:
        return n
    elif n == 2:
        return 1 if abs(A[0]) == abs(A[1]) else 2

    for i in range(n):
        if not A[i]:
            break
        else:
            A[i] = abs(A[i])

    A.sort()
    i = 0; pos = 1; distinct_count = 1    
    while i < n-1:        
        while pos < n and A[i] == A[pos]:
            pos += 1        
        if pos - i == 1:
            distinct_count += 1
            i = pos; pos += 1
        else:    
            i = pos-1
    return distinct_count