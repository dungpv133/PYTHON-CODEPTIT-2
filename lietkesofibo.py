
fibo = []
fibo.append(1)
fibo.append(1)
for i in range(2, 94):
    fibo.append(fibo[i - 1] + fibo[i - 2])

t = int(input())
while(t > 0):
    t -= 1
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    for i in range(a - 1, b):
        print(fibo[i], end= " ")
    print()