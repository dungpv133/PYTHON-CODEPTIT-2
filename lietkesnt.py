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
    n = int(input())
    a = [int(i) for i in input().split()]
    res = []
    for i in a:
        if(snt(i) and i not in res):
            res.append(i)
    for i in res:
        count = 0
        for j in a:
            if(i == j):
                count = count + 1
        print(f"{i} {count}")

if(__name__ == "__main__"):
    main()