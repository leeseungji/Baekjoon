def solution(s):
    answer = []
    
    for i in range(len(s)):
        distance = -1
        for j in range(i-1, -1, -1): #뒤에서부터
            if s[i] == s[j]:
                distance = i - j
                break
        
        answer.append(distance)
    
    return answer