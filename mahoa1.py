t = int(input())
while t > 0:
    t -= 1
    xau = input()
    res = ""
    i = 0
    while(i < len(xau)):
        key = xau[i]
        count = 1
        # if(i == len(xau) - 1):
        j = i + 1
        while(j < len(xau) and xau[j] == key  ):
            count += 1
            j += 1
        res = res + str(count) + key
        i += count
    print(f"{res}")