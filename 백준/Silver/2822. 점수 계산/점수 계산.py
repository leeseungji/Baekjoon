scores = []

for i in range(8):
    score = int(input())
    scores.append((score, i+1)) #점수, 인덱스 저장 # 튜플 !!!!!

 #점수 내림차순 (인덱스 포함 x)
scores.sort(key = lambda x: x[0] , reverse = True)

#점수
print(sum(score[0] for score in scores[:5]))

#인덱스
score_index = [score[1] for score in scores[:5]]
score_index.sort()

print(' '.join(map(str, score_index)))