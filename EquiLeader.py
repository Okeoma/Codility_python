from itertools import groupby

def solution(A):
    groups = [(i, len(list(j))) for i, j in groupby(sorted(A))]
    n = len(A)
    lead_count = max(groups, key=lambda t: t[1])[1]
    if lead_count <= (n/2): return 0  # not possible
    leader = max(groups, key=lambda t: t[1])[0]
    count = 0
    equi_leaders = 0
    for i in range(n):
        if A[i] == leader: count += 1
        right = lead_count - count
        if count > (i+1)/2 and right > (n-i-1)/2:
            equi_leaders += 1
    return equi_leaders