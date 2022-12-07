

t = int(input())
s = input().split()
s = sorted(s)
# print(s)
res = t + 1
for i in range(t):
    if(int(s[0]) != 1):
        res = 1
        break
    if(i > 0 and int(s[i]) - int(s[i - 1]) > 1):
        res = int(s[i - 1]) + 1
        break
    if(int(s[len(s) - 1]) < t):
        res = int(s[len(s) - 1]) + 1
print(res)    