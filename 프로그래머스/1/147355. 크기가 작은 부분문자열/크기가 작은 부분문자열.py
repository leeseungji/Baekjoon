def solution(t, p):
    answer = 0
    
    len_p = len(p)
    int_p = int(p)
    
    for i in range(len(t) - len_p + 1):
        if int(t[i : i + len_p]) <= int_p:
            answer += 1
    
    return answer