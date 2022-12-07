
def sochuso(n):
    # print(len(n))
    return len(n) % 2 == 1

def soxenke(n):
    if(len(n) > 1 and n[0] == n[1]):
        # print(n[0] != n[1])
        return False
    for i in range(0, len(n), 2):
        if(s[i] != s[0]):
            # print(f"Loi o {i}")
            return False
    return True

t = int(input())
while((t > 0)):
    t -= 1
    s = input()
    if(sochuso(s) and soxenke(s)):
        print("YES")
    else:
        print("NO")