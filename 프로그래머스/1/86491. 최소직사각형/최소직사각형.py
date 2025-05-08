def solution(sizes):
    max_h = 0
    max_w = 0
    
    for w, h in sizes:
        height = min(w,h)
        width = max(w,h)
        
        max_h = max(height, max_h)
        max_w = max(width, max_w)
    
    return max_w * max_h