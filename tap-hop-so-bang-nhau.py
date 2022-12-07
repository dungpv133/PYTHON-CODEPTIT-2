
n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print("YES") if(set(a) == set(b)) else print("NO")