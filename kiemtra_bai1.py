import math

def snt(n):
    n = int(n)
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

n = 30
prime_numbers = [2,3]
i=3
while (True):
        i+=1
        status = True
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                status = False
                break
        if(status==True):
            prime_numbers.append(i)
        if(len(prime_numbers)==n):
            break
print('So nguyen to thu 30 la:', prime_numbers[n-1])
msv = 3
count = 0
for i in range(1, 30 + msv + 1):
    if(snt(i)):
        count += 1
print(f"So luong so nguyen to trong khoang tu 1 den 30 + n voi n = 3 la: {count}")
