def solution(num):
    x = str(num)
    s = 0
    while(True):
        
        for i in x:
            s += int(i)
        if s<=9:
            break
        x = str(s)
        s = 0
    return s

print(solution(493193))
print(solution(942))
print(solution(16))
