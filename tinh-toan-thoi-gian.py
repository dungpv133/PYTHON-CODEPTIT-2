import datetime

class GameThu:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        self.vao = vao
        self.ra = ra
        # self.tg = 0

    def tinhtg(self):
        vao = datetime.datetime.strptime(self.vao, '%H:%M')
        ra = datetime.datetime.strptime(self.ra, "%H:%M")
        self.tg = ra - vao
    def __str__(self):
        self.tg = str(self.tg)
        a = self.tg.split(':')
        return self.ma + "  " + self.ten + " " + a[0] + " gio " + a[1] + " phut"

    def result(self):
        self.tg = str(self.tg)
        print(self.ma, self.ten, end = ' ')
        a = [int(i) for i in self.tg.split(':')]
        print("{} gio {} phut".format(a[0], a[1]))

def main():
    n = int(input())
    a = []
    for i in range(n):
        ma = input()
        ten = input()
        vao = input()
        ra = input()
        a.append(GameThu(ma, ten, vao, ra))
    for i in a:
        i.tinhtg()
    a.sort(key=lambda x: x.tg, reverse=True)
    for i in a:
        i.result()

if(__name__ == "__main__"):
    main()
