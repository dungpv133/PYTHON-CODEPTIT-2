import math

class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    
    @staticmethod
    def cong(a, b):
        thuc = a.thuc + b.thuc
        ao = a.ao + b.ao
        return SoPhuc(thuc, ao)

    @staticmethod
    def nhan(a, b):
        thuc = a.thuc * b.thuc - a.ao * b.ao
        ao = a.thuc * b.ao + a.ao * b.thuc
        return SoPhuc(thuc, ao)
    
def main():
    t = int(input())
    while(t > 0):
        t = t - 1
        arr = [int(i) for i in input().split()]
        a = SoPhuc(arr[0], arr[1])
        b = SoPhuc(arr[2], arr[3])
        tong = SoPhuc.cong(a, b)
        c = SoPhuc.nhan(tong, a)
        d = SoPhuc.nhan(tong, tong)
        dau1 = ""
        dau2 = ""
        if(c.ao < 0):
            c.ao = -c.ao
            dau1 = "-"
        else:
            dau1 = "+"
        if(d.ao < 0):
            d.ao = -d.ao
            dau2 = "-"
        else:
            dau2 = "+"
        print(f"{c.thuc} {dau1} {c.ao}i, {d.thuc} {dau2} {d.ao}i")

if(__name__ == "__main__"):
    main()