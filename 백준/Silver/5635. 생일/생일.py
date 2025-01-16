n = int(input())
students = []

for _ in range(n):
    student = input().split()
    name = student[0]
    day, month, year = map(int, student[1:])
    
    students.append((year, month, day, name))

students.sort()

print(students[-1][3])
print(students[0][3])