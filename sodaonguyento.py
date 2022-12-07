from math import gcd
t = int(input())
while((t > 0)):
    t -= 1
    s = (input())
    rev = int(''.join(reversed(s)))
    if(gcd(int(s), rev) == 1):
        print("YES")
    else:
        print("NO")