def solution(d, budget):
    
    d.sort()
    answer = 0
    
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            answer+=1
        else:
            break
    
    return answer