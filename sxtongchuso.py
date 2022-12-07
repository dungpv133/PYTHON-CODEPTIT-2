#ca tong va tich chu so

def cmp(n):
    s = str(n)
    sum = 1
    for i in s:
        sum *= ord(i) - ord('0')
    return sum

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]
    arr = sorted(arr)
    arr.sort(key = cmp)
    for i in arr:
        print(i, end= ' ')
    print()