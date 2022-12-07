

t = int(input())
while(t > 0):
    t -= 1
    s = int(input())
    res = []
    s = str(s)
    for i in range(0, len(s)):
        res.append(int(s[i]))    
    res.reverse()
    for i in range(0, len(res) - 1):
        if(res[i] >= 5):
            res[i + 1] += 1
        res[i] = 0
    res.reverse()
    for i in range(0, len(s)):
        print(res[i], end = '')
    print()
