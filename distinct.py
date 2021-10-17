#solution 1
def solution(A):
    list_of_absolute_values = list(map(lambda x:abs(x), A))
    return len(set(list_of_absolute_values))
    


# Best python Solution
# This function prints all distinct elements
def solution(A):
 
    # Creates an empty hashset
    s = set()
     
    # Traverse the input array
    res = 0
    for i in range(len(A)):
     
        # If not present, then put it in
        # hashtable and increment result
        if (A[i] not in s):
            s.add(A[i])
            res += 1
     
    return res


# Wrong solution
def solution(A):
    # write your code in Python 3.6
    count = 1    
    S = list(map(lambda x:abs(x), A))

    for i in range(1,len(A)):    
        if(S[i] != S[i-1]): 
            count+=1
    return count


# Solution 100% JavaScript
function solution(A) {
    var count = 1,
        len = A.length,
        S = A.map(function(x){ return Math.abs(x) }).sort();

    for(var i=1;i<len;i++) {
        if(S[i] != S[i-1]) count++;        
    }

    return count;
}