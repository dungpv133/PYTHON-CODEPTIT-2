import math

def snt(n):
    n = int(n)
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    nt = []
    for i in range(n):
        if(snt(a[i])):
            nt.append(int(a[i]))
    count = 0
    nt.sort()
    for i in range(n):
        if(snt(a[i])):
            print(f"{nt[count]}", end = " ")
            count += 1
        else:
            print(a[i], end = " ")

if(__name__ == "__main__"):
    main()