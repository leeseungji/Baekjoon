def solution(a, b):
    
    yoil = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    nums = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    return yoil[(sum(nums[:a-1]) + b -1) % 7]
