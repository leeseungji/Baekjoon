from collections import Counter
n = int(input())
titles = []
for i in range(n):
    title = input().strip()
    titles.append(title)

title_counter = Counter(titles) #책 제목 수 딕셔너리로
max_title_counter = max(title_counter.values( )) #가장 많은 책 제목 수 : 숫자만 출력

#베스트셀러 제목 구하기
best_seller = []

for title, count in title_counter.items():
    if count == max_title_counter:
        best_seller.append(title)
 
best_seller.sort()
print(best_seller[0])
