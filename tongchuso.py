
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    chu = []
    so = 0
    for i in s:
        if(i.isalpha()):
            chu.append(i)
        else:
            so += int(i)
    chu.sort()
    for i in chu:
        print(i, end="")
    print(so)