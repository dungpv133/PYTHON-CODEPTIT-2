

t = int(input())
while(t > 0):
    t -= 1
    s = input().split()
    n = float(s[0])
    x = float(s[1])
    m = float(s[2])
    count = 0
    sum = n * (1 + x / 100) ** count
    while(sum < m):
        count += 1
        sum = n * (1 + x / 100) ** count
    print(count)
    