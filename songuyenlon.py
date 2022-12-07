import math

def ucln(a, b):
    a = int(a)
    b = int(b)
    while(a * b != 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
    return a + b

def main():
    t = int(input())
    while(t > 0):
        t = t - 1
        a = int(input())
        b = input()
        du = 0
        for i in range(len(b)):
            du = du * 10 + int(b[i])
            du = du % a
        print(ucln(a, du))

if(__name__ == "__main__"):
    main()