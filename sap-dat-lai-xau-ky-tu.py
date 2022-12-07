

t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    kt = True
    if(len(s1) != len(s2)):
        kt = False
    else:
        for j in s1:
            if(s1.count(j) != s2.count(j)):
                kt = False
                break
    if(kt):
        kt = "YES"
    else:
        kt = "NO"
    print(f"Test {i + 1}: {kt}")