import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = int(tu)
        self.mau = int(mau)
    
    def toiGian(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln
        return self

def main():
    a = (input().split())
    tu = int(a[0])
    mau = int(a[1])
    ps = PhanSo(tu, mau)
    ps = ps.toiGian()
    print(f"{ps.tu}/{ps.mau}")

if(__name__ == "__main__"):
    main()