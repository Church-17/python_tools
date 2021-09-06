from itertools import repeat

def true_primes(n: int) -> list[bool]:
    nodd = (n - 1)//2
    is_prime = [True] * nodd
    for p in range(int((n**.5 - 1)/2)):
        if is_prime[p]:
            is_prime[2*p**2 + 6*p + 3 :: 2*p + 3] = repeat(False, len(range(2*p**2 + 6*p + 3, nodd, 2*p + 3)))
    return [True] + is_prime

countPrimes = lambda n : sum(n)

def listPrimes(n: list[bool]) -> list[int]:
    return [2] + [2*i + 3 for i in range(len(n) - 1) if n[i + 1]]

def main():
    from time import time
    target = 10201
    start = time()
    out = true_primes(target)
    elapsed = time() - start
    print(sum(out))
    print('Done in: ', elapsed)

if __name__ == '__main__':
    main()