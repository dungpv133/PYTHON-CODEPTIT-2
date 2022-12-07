import math
def snt(n):
    n = int(n)
    if((n) < 2):
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

def main():
    a = (input().split(' '))
    n = int(a[0])
    m = int(a[1])
    res = []
    for i in range(n):
        a = [int(i) for i in input().split()]
        temp = []
        for j in range(m):
            if(snt(a[j])):
                temp.append(1)
            else:
                temp.append(0)
        res.append(temp)
    for i in range(n):
        for j in range(m):
            print((res[i][j]), end=" ")
        print()

if(__name__ == "__main__"):
    main()
