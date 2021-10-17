# Solution 1
solution(X, Y, D)
    p = 0
    while (X < Y)
        p+=1
        X = X + D        
    return p    
    
# Solution 2    
solution(X, Y, D)
    return math.ceil((Y - X) / D)
    