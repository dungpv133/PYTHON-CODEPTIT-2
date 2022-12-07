

t = int(input())
while((t > 0)):
    t -= 1
    s = int(input())
    sum = 0
    if(s % 2 == 0):
        for i in range(2, s + 1, 2):
            sum += 1 / i
    else:
        for i in range(1, s + 1, 2):
            sum += 1 / i
    print("{:.6f}".format(sum))