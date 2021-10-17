def solution(N, P, Q):
    A=len(P)*[0]
    if N<4:
        return A    
    Factor = [0] * (N + 1)
    i = 2
    while (i * i <= N):
        if (Factor[i] == 0):
            k = i * i
            while (k <= N):
                if (Factor[k] == 0):
                    Factor[k] = i
                k += i
        i += 1    
    Incluse_scan=[0] * (N + 1)
    cnt_semi=0
    for k in range(4,N+1):
        if Factor[k]!=0:
            d=int(k/Factor[k])
            if Factor[d]==0:
                cnt_semi+=1                 
        Incluse_scan[k]=cnt_semi     
    for r in range(0,len(P)):
        if(P[r]<=4):
            min_inclusive=0
        else:
            min_inclusive=P[r]-1 
        A[r]=Incluse_scan[Q[r]]-Incluse_scan[min_inclusive] 
    return A
    
    
# Solution 2
def solution(N, P, Q):
 A=len(P)*[0]
 if N<4:
     return A
#Minimum prime factor of n stored in Factor[n]
 Factor = [0] * (N + 1)
 i = 2
 while (i * i <= N):
  if (Factor[i] == 0):
   k = i * i
   while (k <= N):
    if (Factor[k] == 0):
     Factor[k] = i;
    k += i
  i += 1
#Count semi prime numbers and store 
#sum scan in array Incluse_scan   
 Incluse_scan=[0] * (N + 1)
 cnt_semi=0
 for k in range(4,N+1):
     if Factor[k]!=0:
         d=int(k/Factor[k])
         if Factor[d]==0:
             cnt_semi+=1                 
     Incluse_scan[k]=cnt_semi   
#Do the difference of semi prime counters
 for r in range(0,len(P)):
     if(P[r]<=4):
       min_inclusive=0
     else:
       min_inclusive=P[r]-1 
     A[r]=Incluse_scan[Q[r]]-Incluse_scan[min_inclusive] 
 return A