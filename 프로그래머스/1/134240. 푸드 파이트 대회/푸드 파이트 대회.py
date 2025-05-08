def solution(food):
    answer = ''
    
    for i in range (len(food)):
        count = food[i] // 2
        answer += str(i) * count
    
    
    return answer + '0' + answer[::-1]