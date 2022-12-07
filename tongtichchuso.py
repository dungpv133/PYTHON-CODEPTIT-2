#ca bai tich va tong chu so

t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    sum = 0
    mul = 1
    kt = False
    for i in range(len(s)):
        if(i % 2 != 0):
            sum += int(s[i])
        else:
            if(int(s[i]) != 0):
                mul *= int(s[i])
                kt = True
    if(not kt):
        mul = 0
    print(f"{mul} {sum}")
