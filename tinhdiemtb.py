
t = int(input())
arr = [float(i) for i in input().split()]
arr.sort()
s = float(arr[0])
b = float(arr[-1])
sum = 0
for i in arr:
    i = float(i)
    if(i != b and i != s):
        sum += i
    else:
        t -= 1
# print(f"{sum} {t}")
print("{:.2f}".format(sum / t))