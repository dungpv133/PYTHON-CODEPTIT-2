from math import gcd

s = input().split()
n = int(s[0])
k = int(s[1])
dem = 0
for i in range(10 ** (k - 1), 10 ** k):
    if(gcd(n, i) == 1):
        print(i, end = ' ')
        dem += 1
        if(dem == 10):
            print()
            dem = 0