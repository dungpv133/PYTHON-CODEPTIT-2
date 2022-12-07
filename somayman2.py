t = int(input())
while(t > 0):
    t -= 1
    s = input()
    kt = True
    for i in s:
        if(int(i) != 4 and int(i) != 7):
            kt = False
            break
    if(kt):
        print("YES")
    else:
        print("NO")