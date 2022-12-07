
n = input()
so = ''.join(n.split('688'))
so = ''.join(so.split('68'))
so = ''.join(so.split('6'))
print("YES") if len(so) == 0 else print("NO")