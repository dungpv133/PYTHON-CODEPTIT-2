# ca snt va so thuan nghich

# def kt(n):
#     if(int(n) < 10):
#         return False
#     temp = int(n)
#     nghich = 0
#     while(temp > 0):
#         nghich = nghich * 10 + int(temp) % 10
#         temp = int(temp / 10)
#     # print(nghich)
#     return nghich == int(n)
import math
def prime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    # print(sum)
    if(prime(sum)):
        print("YES")
    else:
        print("NO")