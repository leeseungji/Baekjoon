import sys

data = sys.stdin.read().strip().split() # 데이터 한 번에 입력받기 (리스트 이용)

n = int(data[0])
nums1 = set(map(int, data[1:n+1]))

m = int(data[n+1])
nums2 = list(map(int, data[n+2:n+2+m]))

result = []
for num in nums2: # num = 1 3 7 9 5
    if num in nums1:
        result.append('1\n')
    else:
        result.append('0\n')
        
sys.stdout.write(''.join(result))