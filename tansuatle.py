

t = int(input())
while((t > 0)):
    t -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    dem = [0] * 100009
    for i in arr:
        dem[i] += 1
    for i in arr:
        if(dem[i] % 2 != 0):
            print(i)
            break