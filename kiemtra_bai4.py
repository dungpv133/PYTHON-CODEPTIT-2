def solapphuong(n):
    n = abs(int(n))
    return round(n ** (1 /3)) ** 3 == n

def sochinhphuong(n):
    n = int(n)
    if n < 0:
        return False
    return round(n ** (1 / 2)) ** 2 == n


def sotunhien(n):
    return n >= 0


so = int(input("Nhap vao mot so: "))
if(solapphuong(so)):
    print(f"{so} la so lap phuong")
if(sochinhphuong(so)):
    print(f"{so} la so chinh phuong")

if(solapphuong(so) == False and sochinhphuong(so) == False and sotunhien(so)):
    print(f"{so} la so tu nhien")

