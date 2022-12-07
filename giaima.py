n = int(input())

while n > 0:
    n -= 1
    xau = input()
    res = ""
    for i in range(0, len(xau), 2):
        num = int(xau[i + 1])
        for j in range(num):
            res = res + xau[i]
    print(res)