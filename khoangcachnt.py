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
    list_snt = []
    num = 1
    while(len(list_snt) < 1001):
        num = num + 1
        if(snt(num)):
            list_snt.append(int(num))
    a = [int(i) for i in input().split()]
    n = a[0]
    x = a[1]
    for i in range(n + 1):
        print(x, end = " ")
        x = x + list_snt[i]
    print()

if(__name__ == "__main__"):
    main()