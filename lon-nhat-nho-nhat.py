
while(True):
    n = int(input())
    if(n == 0):
        break
    a = []
    for i in range(n):
        a.append(int(input()))
    if(max(a) != min(a)):
        print(f"{min(a)} {max(a)}")
    else:
        print("BANG NHAU")