
t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    mul = 1
    for i in s:
        i = int(i)
        if(i != 0):
            mul *= i
    print(mul)