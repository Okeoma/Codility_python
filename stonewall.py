# This is the solution for Stacks And Queues > StoneWall
#
# This is marked as PAINLESS difficulty


def solution(H):
    stack =[]
    count = 1

    stack.append(H[0])
    for i in range(1,len(H)):
        if len(stack) == 0:
            stack.append(H[i])
            count+=1
        if H[i] > stack[-1]:
            stack.append(H[i])
            count+=1
        while H[i] < stack[-1]:
            stack.pop()
            if len(stack) == 0:
                stack.append(H[i])
                count+=1
            elif H[i] > stack[-1]:
                stack.append(H[i])
                count+=1
    return count