import math
n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr), 1):
        if(math.gcd(arr[i], arr[j]) == 1):
            print(f"{arr[i]}  {arr[j]}")