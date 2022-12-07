
t = int(input())
while(t > 0):
    t = t - 1
    s = input()
    num = []
    kt = True
    for i in range(len(s)):
        if(s[i] != '0' and s[i] != '1' and s[i] != '2'):
            kt = False
            break
    if(kt):
        print("YES")
    else:
        print("NO")