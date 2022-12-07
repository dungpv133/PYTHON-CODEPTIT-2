t = int(input())
while t > 0:
    t -= 1
    num = input()
    if len(num) > 1 and int(num[-1]) == 6 and int(num[-2]) == 8:
        print("YES\n")
    else:
        print("NO\n")