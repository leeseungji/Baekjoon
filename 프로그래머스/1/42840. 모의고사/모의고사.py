def solution(answers):
    answer = []
    
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0] * 3
    
    for i in range (len(answers)):
        if answers[i] == patterns[0][i % len(patterns[0])]:
            scores[0] += 1
        
        if answers[i] == patterns[1][i % len(patterns[1])]:
            scores[1] += 1
        
        if answers[i] == patterns[2][i % len(patterns[2])]:
            scores[2] += 1
        
    max_scores = max(scores)
    
    for i in range(3):
        if max_scores == scores[i]:
            answer.append(i + 1)
    
    return answer