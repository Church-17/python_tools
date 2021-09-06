def prime(n: int):
    if n == 2 or n == 5:
        return True
    if n%2 == 0 or n%5 == 0:
        return False
    sqrt = int(n**.5) + 1
    for div in range(3, sqrt, 10):
        if n%div == 0:
            return False
    for div in range(7, sqrt, 10):
        if n%div == 0:
            return False
    for div in range(11, sqrt, 10):
        if n%div == 0:
            return False
    for div in range(19, sqrt, 10):
        if n%div == 0:
            return False
    return True

def goldbach(n: int):
    if n < 2:
        return False, False
    if n == 2:
        return 2, 2
    for p in range(3, n, 2):
        q = 2*n - p
        if prime(p) and prime(q):
            return p, q

from time import time
i = int(input('Inserire un numero: '))
start = time()
p1, p2 = goldbach(i)
print('= (', p1, '+', p2, ') / 2')
print('Time:', time() - start, 'seconds')