month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

m, d = map(int, input().split())

total = sum(month[:m-1]) + d

print(week[total % 7])
