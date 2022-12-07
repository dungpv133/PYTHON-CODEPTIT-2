import math

class PhanSo:
    def __init__(self, tu1, mau1, tu2, mau2):
        self.tu1 = int(tu1)
        self.tu2 = int(tu2)
        self.mau1 = int(mau1)
        self.mau2 = int(mau2)

    @staticmethod    
    def toiGian(tu, mau):
        ucln = math.gcd(tu, mau)
        tu = tu // ucln
        mau = mau // ucln
        print(f"{tu}/{mau}")

    def cong(self):
        tu = self.tu1 * self.mau2 + self.tu2 * self.mau1
        mau = self.mau1 * self.mau2
        self.toiGian(tu, mau)
        

def main():
    a = (input().split())
    tu1= int(a[0])
    tu2 = int(a[2])
    mau1 = int(a[1])
    mau2 = int(a[3])
    ps = PhanSo(tu1, mau1, tu2, mau2)
    ps.cong()

if(__name__ == "__main__"):
    main()