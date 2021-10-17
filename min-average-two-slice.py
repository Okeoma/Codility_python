import sys

def solution(A):
    # write your code in Python 3.6
    n             = len(A)
    pre_sum       = [0] * (n+1)
    min_slice_avg = sys.maxsize
    min_slice_idx = 0

    for i in range(1,n+1):
        pre_sum[i] = pre_sum[i-1] + A[i-1]

        # calculate at least 2 prefix sums
        if i-2 < 0: continue

        # check prev 3 slices if we have calculated 3 prefix sums
        if i>=3:
            prev_3_slice_avg = (pre_sum[i] - pre_sum[i-3]) / 3.0

            if prev_3_slice_avg < min_slice_avg:
                min_slice_avg = prev_3_slice_avg
                min_slice_idx = i-3

        # check prev 2 slices
        prev_2_slice_avg = (pre_sum[i] - pre_sum[i-2]) / 2.0

        if prev_2_slice_avg <  min_slice_avg:
            min_slice_avg = prev_2_slice_avg
            min_slice_idx = i-2
    return min_slice_idx