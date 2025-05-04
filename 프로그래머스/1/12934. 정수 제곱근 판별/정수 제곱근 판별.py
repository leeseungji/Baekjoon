import math

def solution(n):
    answer = 0
    
    if math.isqrt(n) ** 2 == n:
        answer = (math.isqrt(n) + 1) ** 2
        
    else:
        answer = -1
    
    return answer