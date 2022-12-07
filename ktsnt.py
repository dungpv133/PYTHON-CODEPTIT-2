import math
def snt(n):
    if(n < 2):
        return 0
    for i in range(3, math.sqrt(n)):
        if(n % i == 0):
            return 0
    return 1

