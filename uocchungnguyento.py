import math

def prime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def ucln(a, b):
    a = int(a)
    b = int(b)
    while(a * b != 0):
        if(a > b):
            a %= b
        else:
            b %= a
    return a + b

def kt(a, b):
    u = ucln(a, b)
    sum = 0
    # print(u)
    while(u > 0):
        sum += u % 10
        u = int(u / 10)
    # print(sum)
    if(prime(sum)):
        print("YES")
    else:
        print("NO")

t = int(input())
while(t > 0):
    t -= 1
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    kt(a, b)

    