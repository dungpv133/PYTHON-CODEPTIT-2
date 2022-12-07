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

t = int(input())
while(t > 0):
    t -= 1
    s = int(input())
    sum = 0
    for i in range(1, s):
        if(ucln(i, s) == 1):
            sum += 1
        
    if(prime(sum)):
        print("YES")
    else:
        print("NO")
