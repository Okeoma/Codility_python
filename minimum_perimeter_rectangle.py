# Solution

def solution(N):
    # write your code in Python 3.6
    minN = 1+N
    i=1
    while(i*i<=N):
        if(N % i == 0):
            minN = min(minN, N//i+i)
        i+=1         
    return 2*minN
    
    
 #Java solution
 class Solution {
    public int solution(int N) {
        int min = 1+N;
        int i=1;
        while(i*i<=N) {
            if(N % i == 0) {
                min = Math.min(min, N/i+i);
            }
            i++;
        }
        return 2*min;
    }
}
