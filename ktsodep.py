
t = int(input())
while(t > 0):
    t = t - 1
    s = input()
    num = []
    kt = True
    for i in range(len(s) - 2):
        if(s[i] != s[i + 2] or len(num) > 2):
            kt = False
            break
        if(s[i] not in num):
            num.append(s[i])
    if(len(num) > 2):
        kt = False
    if(kt):
        print("YES")
    else:
        print("NO")