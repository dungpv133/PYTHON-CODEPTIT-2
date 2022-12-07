
class Rectangle:
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color.lower().title
    
    def kt(self):
        if(self.a > 0 and self.b > 0):
            return True
        return False

    def perimeter(self):
        return self.a * 2 + self.b * 2
    
    def area(self):
        return self.a * self.b
    


t = 1
while t > 0:
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]),arr[2])
    if(r.kt()):
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    else:
        print("INVALID")
    t -= 1