import math

def snt(n):
    n = int(n)
    if(n < 2):
        return False
    for i in range(3, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

def kt(n):
    if(not snt(len(n))):
        # print("loi 0")
        return False
    count = 0
    for i in n:
        if(not snt(i)):
            # print("loi 1")
            return False
        count += int(i)
    if(not snt(count)):
        # print("loi 2")
        return False
    if(not snt(n) or not snt(n[:: -1])):
        # print("loi 3")
        return False
    return True

def main():
    t = int(input())
    while(t > 0):
        t -= 1
        if(kt(input())):
            print("Yes")
        else:
            print("No")

if(__name__ == "__main__"):
    main()