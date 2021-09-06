def fib_lim(n: int):
    out = []
    a, b = 0, 1
    while a < n:
        out.append(a)
        a, b = b, a + b
    return out

def fib_term(n: int):
    out = []
    a, b = 0, 1
    for _ in range(n + 1):
        out.append(a)
        a, b = b, a + b
    return out

from time import time
i = int(input('Ins: '))
start = time()
print(fib_term(i))
print('Time:', time() - start, 'seconds')