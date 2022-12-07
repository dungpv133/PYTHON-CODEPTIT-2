test1 = int(input())
while (test1 > 0):
    test1 -= 1
    n = int(input())
    a = input()
    a = a.split(' ')
    b = set(a)
    kt = False
    res = 0
    for num in b:
      if(a.count(num) > n / 2):
            kt = True
            res = num
            break
    if(kt):
        print(res)
    else:
        print('NO')