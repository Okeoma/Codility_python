from math import sqrt

def solution(N):
    DiViSoRs = 0
    sqrtN = int(sqrt(N))+1
    for factor in range(1,sqrtN):
        if N % factor == 0:
            if N/factor == factor:
                DiViSoRs += 1
            else:
                DiViSoRs += 2
    return DiViSoRs