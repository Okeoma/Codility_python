def solution(A):
    length = len(A)
    if length <= 2:
        return 0

    peek_indexes = []
    for index in range(1, length-1):
        if A[index] > A[index - 1] and A[index] > A[index + 1]:
            peek_indexes.append(index)

    for block in range(3, int((length/2)+1)):
        if length % block == 0:
            index_to_check = 0
            temp_blocks = 0
            for peek_index in peek_indexes:
                if peek_index >= index_to_check and peek_index < index_to_check + block:
                    temp_blocks += 1
                    index_to_check = index_to_check + block
            if length/block == temp_blocks:
                return temp_blocks

    if len(peek_indexes) > 0:
        return 1
    else:
        return 0
print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2, 1, 2, 5, 2]))