def prime(n):
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

if __name__ == '__main__':
    from time import time
    target = int(input('Ins: '))
    start = time()
    print(len(prime(target)))
    elapsed = time() - start
    print('Time: ', elapsed)