def solution(n):
    answer = ''
    
    an = '수박' * (n // 2)
    
    if n % 2 == 1:
        answer = f"{an}수" 
    else:
        answer = f"{an}"
    
    return answer