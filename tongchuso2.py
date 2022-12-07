
s = input()
count = 0
while(len(s) > 1):
    temp = 0
    for i in s:
        temp += int(ord(i) - ord('0'))
    s = str(temp)
    count += 1
print(count)
