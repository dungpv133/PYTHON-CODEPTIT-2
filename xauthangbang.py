n = int(input())
while(n > 0):
    n -= 1
    s = input()
    kt = True
    for i in range(0, int(len(s) / 2)):
        if(abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[-1 - i]) - ord(s[-2- i]))):
            kt = False
            break
    if(kt):
        print("YES")
    else:
        print("NO")