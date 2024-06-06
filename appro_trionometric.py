import math

#factor of a number
def factor(x):
    total = 1
    for i in range(1, x+1, 1):
        total *= i
        
    return total



def appro_sin(x, n):
    sin = 0
    for i in range(0, n, 1):
        sin = sin + (-1)**i * ((x**(2*i + 1)) / (factor(2*i + 1)))
    return sin


def appro_cos(x, n):
    cos = 0
    for i in range(0, n, 1):
        cos = cos + (-1)**i * ((x**(2*i)) / (factor(2*i)))
    return cos

def appro_sinh(x, n):
    sinh = 0
    for i in range(0, n, 1):
        sinh = sinh + ((x**(2*i + 1)) / (factor(2*i + 1)))
    return sinh

def appro_cosh(x, n):
    cosh = 0
    for i in range(0, n, 1):
        cosh = cosh + ((x**(2*i)) / (factor(2*i)))
    return cosh


#print(appro_cosh(x = 3.14,n = 10))