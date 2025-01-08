n = int(input()) #숫자 개수 입력 5
nums_list = []

for i in range(n): # 숫자 5개 입력 
    num = int(input())
    nums_list.append(num)

sorted_nums = sorted(nums_list)

print('\n'.join(map(str, sorted_nums)))