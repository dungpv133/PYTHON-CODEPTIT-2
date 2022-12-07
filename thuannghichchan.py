import math

def kt(n):
    n = str(n)
    m = n[ :: -1]
    if(n != m or len(n) % 2 != 0):
        return False
    for i in m:
        if(int(i) % 2 != 0):
            return False
    return True

def thuannghich(n):
    for i in range(22, n, 22):
        if(kt(i)):
            print(i, end=" ")

if(__name__ == "__main__"):
    t = int(input())
    while t > 0:
        t = t - 1
        thuannghich(int(input()))
        print()
