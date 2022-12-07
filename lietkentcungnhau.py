import math

n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if(math.gcd(a[i], a[j]) == 1):
            print(f"{a[i]} {a[j]}")
