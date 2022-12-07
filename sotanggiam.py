
t = int(input())
while(t > 0):
    t = t - 1
    a = input()
    kt = True
    for i in range(1, len(a)):
        if(a[i] == a[i - 1]):
            kt = False
            break
        elif(a[i] < a[i - 1]):
            for j in range(i + 1, len(a)):
                if(a[j] >= a[j - 1]):
                    kt = False
                    break
            break
        else:
            continue
    if(kt and len(a) > 2):
        print("YES")
    else:
        print("NO")