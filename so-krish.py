from math import factorial

def kt(n):
    giaithua = 0
    for i in n:
        giaithua += factorial(int(i))
    return giaithua == int(n)

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