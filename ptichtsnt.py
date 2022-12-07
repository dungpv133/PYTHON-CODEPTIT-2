import math

t = int(input())
while(t > 0):
    t -= 1
    s = int(input())
    res = "1 "
    for i in range(2, s + 1):
        if(s % i == 0):
            count = 0
            while(s % i == 0):
                count += 1
                s = int(s / i)
            res = res + "* " + str(i) + "^" + str(count) + " "
    print(res)