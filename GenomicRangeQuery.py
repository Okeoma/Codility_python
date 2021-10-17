def solution(S, P, Q):

    count = []
    for i in range(3):
        count.append([0]*(len(S)+1))

    for index, i in enumerate(S):
        count[0][index+1] = count[0][index] + ( i =='A')
        count[1][index+1] = count[1][index] + ( i =='C')
        count[2][index+1] = count[2][index] + ( i =='G')

    result = []

    for i in range(len(P)):
      start = P[i]
      end = Q[i]+1

      if count[0][end] - count[0][start]:
          result.append(1)
      elif count[1][end] - count[1][start]:
          result.append(2)
      elif count[2][end] - count[2][start]:
          result.append(3)
      else:
          result.append(4)

    return result

