n = int(input())
member = []

for i in range(n):
    age, name = input().split()
    member.append((int(age), i, name)) #sort 안정정렬) 세번째 요소까지 영향 x -> i추가
 
member.sort()

for age,i, name in member:
    print(age, name)
