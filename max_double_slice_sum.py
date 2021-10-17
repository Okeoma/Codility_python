# Solution
def solution(A):
    ar_len = len(A)
    ending_here_sum = [0] * ar_len
    starting_here_sum = [0] * ar_len
    
    for index in range(1, ar_len - 2):  
        ending_here_sum[index] = max(ending_here_sum[index - 1] + A[index], 0)   
    for index in range(ar_len - 2, 1, -1):
        starting_here_sum[index] = max(starting_here_sum[index + 1] + A[index], 0)    
    max_slice_sum = ending_here_sum[0] + starting_here_sum[2]
    for index in range(1, ar_len - 1):
        max_slice_sum = max(max_slice_sum, ending_here_sum[index - 1] + starting_here_sum[index + 1])
    return max_slice_sum


def solution(A):
    ar_len = len(A)
    ending_here_sum = [0] * ar_len
    starting_here_sum = [0] * ar_len

    # the maximum sum contiguous sub sequence ending at index i
    for index in range(1, ar_len - 2):  # A[X + 1] + A[X + 2] + ... + A[Y - 1]
        ending_here_sum[index] = max(ending_here_sum[index - 1] + A[index], 0)

    # the maximum sum contiguous sub sequence starting with index i
    for index in range(ar_len - 2, 1, -1):  # A[Y + 1] + A[Y + 2] + ... + A[Z - 1]
        starting_here_sum[index] = max(starting_here_sum[index + 1] + A[index], 0)

    # Double slice sum should be the maximum sum of ending_here_sum[i-1]+starting_here_sum[i+1]
    max_slice_sum = ending_here_sum[0] + starting_here_sum[2]
    for index in range(1, ar_len - 1):
        max_slice_sum = max(max_slice_sum, ending_here_sum[index - 1] + starting_here_sum[index + 1])

    return max_slice_sum