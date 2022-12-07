import math

def prime(n):
    num = int(n)
    if(num < 2):
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if(num % i == 0):
            return False
    return True

def kt(n):
    if(not prime(len(n))):
        return False
    co = 0
    ko = 0
    for i in n:
        if(prime(int(i))):
            co += 1
        else:
            ko += 1
    return co > ko    

    
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    if(kt(s)):
        print("YES")
    else:
        print("NO")