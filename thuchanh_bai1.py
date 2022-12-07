
#bai 1
# class Number:
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2
#     def input_info(self):
#         print(f"{self.number1} \t {self.number2}")

#     def addition(self):
#         return (self.number1 + self.number2)

#     def subtract(self):
#         return (self.number1 - self.number2)

#     def multi(self):
#         return (self.number1 * self.number2)
    
#     def division(self):
#         return (self.number1 / self.number2)


# demo_num = Number(10, 22)
# demo_num.input_info()
# print(demo_num.addition())
# print(demo_num.subtract())
# print(demo_num.multi())
# print(demo_num.division())

#bai 2
import math
class Prime:
    def __init__(self):
        pass
    def isprime(self, new_num):
        if(new_num < 2):
            return False
        for i in range(3, int(math.sqrt(new_num)) + 1):
            if(new_num % i == 0):
                return False
        return True

    def nextprime(self, next_num):
        while(True):
            next_num += 1
            if(self.isprime(next_num)):
                return next_num

# num_demo = Prime()
# print(num_demo.isprime(14))
# print(num_demo.nextprime(14))

# bai 3
# class Circle:
#     def __init__(self, tam, r : int):
#         self.tam = tam
#         self.r = r
        
#     def describe_circle(self):
#         print(f"Hinh tron tam O{self.tam} ban kinh {self.r}")
        
#     def get_perimeter(self):
#         return self.r * 2 * 3.14

#     def get_area(self):
#         return self.r * self.r * 3.14

# tron = Circle((1, 2), 3)
# tron.describe_circle()
# print(tron.get_area())
# print(tron.get_perimeter())

# bai 4
# class Matrix:


#bai 5
class CheckNumber(Prime):
    def __init__(self, n):
        super().__init__()
        self.n = n
    
    def is_prime(self):
        return super().isprime(self.n)

    def party_check(self):
        return self.n % 2 == 0
    
    def is_perfect(self):
        sum = 0
        for i in range(1, int(self.n / 2)):
            if(self.n % i == 0):
                sum += i
        return sum == self.n

    def is_square(self):
        if(math.sqrt(self.n) - math.floor(math.sqrt(self.n))):
            return False
        return True 


num_demo = CheckNumber(5)
print(num_demo.party_check())
print(num_demo.isprime(num_demo.n))
print(num_demo.is_perfect())
print(num_demo.is_square())