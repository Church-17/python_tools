def factorize(n):
    divs = {}
    exp = 0
    div = 3
    sqrt = n**.5
    while n%2 == 0:
        exp += 1
        n = n//2
        divs[2] = exp
    while n > 1:
        exp = 0
        if div > sqrt:
            divs[n] = 1
            return divs
        while n%div == 0:
            exp += 1
            n = n//div
            divs[div] = exp
        div += 2
    return divs

def main():
    from time import time
    i = int(input('Inserire un numero: '))
    start = time()
    f = factorize(i)
    elapsed = time() - start
    for n in f:
        if f[n] == 1:
            print(n)
        else:
            print(n, '^', f[n])
    print('Done in:', elapsed, 'seconds')

if __name__ == '__main__':
    main()