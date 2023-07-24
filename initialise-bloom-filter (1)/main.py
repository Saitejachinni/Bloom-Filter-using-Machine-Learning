import math

size = 0
seed1, seed2, seed3, seed4, seed5 = 7689571, 15485863, 98899, 71287, 101653

def selectPrime(k):
    for i in range(1, total_prime):
        if prime[i] > k:
            return i

def initSeed():
    global seed1, seed2, seed3, seed4, seed5
    seed1 = 7689571
    seed2 = 15485863
    seed3 = 98899
    seed4 = 71287
    seed5 = 101653

def error(m, n):
    return math.pow((1 - math.exp(-2 * n / m)), 2)

def memory(n, err):
    return int(-(n * math.log(err)) / math.pow(math.log(2), 2))

def number(m, err):
    return int(-(m * math.pow(math.log(2), 2)) / math.log(err))

def setDim(m):
    k = m // (2 * 64)
    f = int(math.sqrt(k))
    i = selectPrime(f)
    a = prime[i // 2 + 3]
    b = prime[i // 2 - 3]
    dim(a, b)
    print("2DBF dimensions:")
    print(a, b)
    size += (a * b) * 64



def free_keyBF(b2):
    _free_(b2)

