n = int(input())

students = []

for i in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    students.append((name, kor, eng, math))

students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0])) #- : 내림차순, +: 오름차순

for student in students:
    print(student[0])