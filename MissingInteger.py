#Solution 1
from itertools import count, filterfalse 

def solution(a):
    return(next(filterfalse(set(a).__contains__, count(1))))
    
#Solution 2   
def solution(A):
    # write your code in Python 3.6
    B = set(A)
    ans = 1
    while ans in B:
       ans += 1
    return ans

    
#Solution 3    
def solution(A):
    # write your code in Python 3.6
    B = set(sorted(A))
    m = 1
    for x in B:
        if x == m:
            m+=1
    return m
  
#Solution 4  
N = set(range(1, 100001))
def solution(A):
    return min(N-set(A))