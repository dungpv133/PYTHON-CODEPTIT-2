
n = int(input())
a = []
b = []
for i in range(n):
    temp = [int(i) for i in input().split()]
    b.append(temp)
if(n == 2):
    print(f"{b[0][1] // 2} {b[0][1] // 2}")
else:

    for i in range(1, n - 1):
        a.append((b[i - 1][i] + b[i][i + 1] - b[i - 1][i + 1]) // 2)
    dau = b[0][1] - a[0]
    cuoi = b[0][n - 1] - dau
    print(dau, end=" ")
    for i in a:
        print(i, end=" ")
    print(cuoi)
