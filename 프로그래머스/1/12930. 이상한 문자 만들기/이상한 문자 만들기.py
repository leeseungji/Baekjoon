def solution(s):
    answer = ''
    
    word_index = 0
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            word_index = 0
        
        else:
            if word_index % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
                
            word_index += 1
    
    
    return answer