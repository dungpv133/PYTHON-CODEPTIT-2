
arr = input().split()
m = int(arr[0])
n = int(arr[1])
b = set()
a = [int(i) for i in input().split()]
a = sorted(set(a))
b = [int(i) for i in input().split()]
b = sorted(set(b))
for i in a:
    if i in b:
        print(i, end=" ")
print()
for i in a:
    if i not in b:
        print(i, end=" ")
print()
for i in b:
    if i not in a:
        print(i, end=" ")
print()