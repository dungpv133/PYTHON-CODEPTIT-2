import math

def main():
    n = int(input())
    mt = []
    for i in range(n):
        temp = [int(j) for j in input().split()]
        mt.append(temp)
    k = int(input())
    sum_up = 0
    sum_down = 0
    for i in range(n):
        for j in range(n):
            if(i > j):
                sum_down = sum_down + mt[i][j]
            elif(i < j):
                sum_up = sum_up + mt[i][j]
    if(abs(sum_down - sum_up) > k):
        print("NO")
    else:
        print("YES")
    print(abs(sum_down - sum_up))

if(__name__ == "__main__"):
    main()