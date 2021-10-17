import time

def gen_fib(n):
    fn = [0] * n
    fn[1] = 1
    for i in range(2, n):
        fn[i] = fn[i-2] + fn[i-1]
    return fn

def solution(A, B):
    n = len(A)    
    fn_series = gen_fib(n+2)[1:]     
    pB = {i: (2**i) -1 for i in range(1, 31)}
    result = [fn_series[A[i]]&(pB[B[i]]) for i in range(n)]    
    return result