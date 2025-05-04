def solution(price, money, count):
    
    ans = 0
    for i in range(1, count+1):
        ans += price * i
        
    if ans > money:
        answer = ans - money
            
    else:
        return 0
        

    return answer