
n = int(input())
arr = []
while(len(arr) < n):
    temp = [int(i) for i in input().split()]
    for j in temp:
        arr.append(j)
arr = [int(i) for i in arr]
chan = []
le = []
for i in range(0, n):
    if(arr[i] % 2 == 0):
        chan.append(int(arr[i]))
    else:
        le.append(int(arr[i]))
chan.sort()
le.sort(reverse = True)
# print(chan)
# print(le)
posChan = 0
posLe = 0
for i in range(n):
    if(arr[i] % 2 != 0):
        print(le[posLe], end=" ")
        posLe += 1
    else:
        print(chan[posChan], end=" ")
        posChan += 1