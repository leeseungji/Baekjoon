def solution(n):
    
    
    result = ''
    while n > 0:
        n,r = divmod(n,3)
        result += str(r)
        
    
    return int(result, 3)