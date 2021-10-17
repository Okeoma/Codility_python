import time

def solution_brute_force(A, B, C):    
    used = 0
    for i in range(len(C)):
        if not A:
            break     
        removed_planks = sorted([j for j in range(len(A)) if A[j] <= C[i] and C[i] <= B[j]], reverse=True)
        
        if removed_planks:            
            for j in removed_planks:
                del A[j]
                del B[j]
        used += 1        
    return -1 if A else used

def find_nail(plank, C):    
    BEGIN_IDX = 0
    END_IDX = 1
    lower = 0
    upper = len(C)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if C[mid] < plank[BEGIN_IDX]:
            lower = mid + 1
        elif C[mid] > plank[END_IDX]:
            upper = mid - 1
        else:
            return True
    return -1

def find_plank(nail, planks):    
    if not planks:
        return -1
    BEGIN_IDX = 0
    END_IDX = 1
    lower = 0
    upper = len(planks)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if planks[mid][BEGIN_IDX] > nail:
            upper = mid - 1
        elif planks[mid][END_IDX] < nail:
            lower = mid + 1
        else: 
            return mid
    return -1


def solution(A, B, C):    
    if max(B) < min(C) or max(C) < min(A):
        return -1 

    planks = sorted(zip(A,B))

    for i in range(len(C)):
        nail = C[i]
        p_idx = find_plank(nail, planks)        
        while p_idx > -1:
            del planks[p_idx]
            p_idx = find_plank(nail, planks)            
        if not planks:            
            return i+1

    return -1