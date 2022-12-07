
t = int(input())
while(t > 0):
    t = t - 1
    n = int(input())
    count = 0
    while(count < 1000 and n % 7 != 0):
        count = count + 1
        dao = str(n)[::-1]
        n = n + int(dao)
    if(n % 7 == 0):
        print(n)
    else:
        print(-1)