import time

def is_valid_minimal_limit(A, num_blocks, sum_slice_limit):
    block_count = 0
    block_sum = 0

    for number in A:
        new = block_sum + number
        if new <= sum_slice_limit:
            block_sum = new
        else:                     
            block_count += 1
            block_sum = number
        if block_count >= num_blocks:
            return False
    return True

def binary_search(A, num_blocks):    
    sum_slice_min = max(A)
    sum_slice_max = sum(A)

    while sum_slice_min <= sum_slice_max:
        sum_slice_mid = (sum_slice_min + sum_slice_max) // 2
        #print(sum_slice_mid)
        if is_valid_minimal_limit(A, num_blocks, sum_slice_mid):
            sum_slice_max = sum_slice_mid - 1
        else:
            sum_slice_min = sum_slice_mid + 1
    
    return sum_slice_min

def solution(K, M, A):    
    return binary_search(A, K)