n = 3
sum = 0
for i in range(1, 200 + n + 1):
    if(i % n == 0):
        sum += i
print(f"Tong cac so chia het cho n tu 1 den 200 + n voi n = 3 la: {sum}")