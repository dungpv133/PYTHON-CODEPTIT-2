while(True):
    chuan = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    xau = input()
    if(xau == '0'):
        break
    chu = xau.split()
    k = int(chu[0])
    s = chu[1]
    res = ''
    for i in s:
        for j in range(0, len(chuan)):
            if(chuan[j] == i):
                res = chuan[(j + k) % 28] + res
    print(res)