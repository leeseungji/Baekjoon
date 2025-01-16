n = int(input())
nums =[]

for _ in range(n):
    num = input().strip()
    nums.append(num)

#우선순위 함수
def function(s):
    int_sum = 0
    for char in s: #a31b -> a 3 1 b
        if char.isdigit():#숫자면 true, 이외 :false
            int_sum += int(char)
    return (len(s), int_sum, s)

nums.sort(key = function)

for num in nums:
    print(num)