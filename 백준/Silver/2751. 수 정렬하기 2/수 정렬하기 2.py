#.sort()

import sys
# 입력: sys.stdin.readline()
# 출력: sys.stdout.readline()

n = int(sys.stdin.readline())
nums_list = []

for i in range(n):# 숫자 5개 입력
    num = int(sys.stdin.readline())
    nums_list.append(num)

nums_list.sort()
    
sys.stdout.write('\n'.join(map(str, nums_list)))