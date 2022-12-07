import math

def prime(n):
    num = int(n)
    if(num < 2):
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if(num % i == 0):
            return False
    return True

def pos(n):
    for i in range(0, len(n)):
        if(prime(i) and not prime(int(n[i]))):
            return False
        elif(not prime(i) and prime(int(n[i]))):
            return False
    return True    

    
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    if(pos(s)):
        print("YES")
    else:
        print("NO")