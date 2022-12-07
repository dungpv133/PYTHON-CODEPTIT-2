import math

def snt(n):
    n = int(n)
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

t = int(input())
while(t > 0):
    t = t - 1
    s = input()
    num = int(s[-4 :: ])
    if(snt(num)):
        print("YES")
    else:
        print("NO")