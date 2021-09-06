import numpy as np
from bisect import bisect_right

def factorize(target: int) -> dict:
    target = np.uint64(target)
    smallest_odd_multiple_of_n_geq_m: int = lambda n, m : m + (n-m) % (2*n)
    primes = np.array([2, 3, 5, 7], dtype=np.uint64)
    index_segment_max = 3
    extend = 7
    segment_min, segment_max = 9, 49
    prime_divs = np.array([], dtype=np.uint64)
    divs = {}
    old_target = 0

    for div in primes:
        if target//div*div == target:
            target = target//div
            prime_divs.resize(len(prime_divs) + 1, refcheck=False)
            prime_divs[-1] = div

    while segment_max < target**.5:
        is_prime = np.full(shape=(segment_max-segment_min)//2, fill_value=True, dtype=bool)
        for p in primes[1:index_segment_max]:
            p = int(p)
            is_prime[(smallest_odd_multiple_of_n_geq_m(p, segment_min) - segment_min) // 2 :: p] = False
        new_primes = np.arange(segment_min, segment_max, 2, dtype=np.uint64)[is_prime]
        for div in new_primes:
            if target//div*div == target:
                target = target//div
                prime_divs.resize(len(prime_divs) + 1, refcheck=False)
                prime_divs[-1] = div
        old_len = len(primes)
        primes.resize(old_len + len(new_primes))
        primes[old_len:] = new_primes
        index_segment_max += extend
        segment_min, segment_max = segment_max, int(primes[index_segment_max]) ** 2
    
    print(new_primes[-1])

    if target**.5 > segment_min:
        is_prime = np.full(shape=int(target**.5 - segment_min + 3)//2, fill_value=True, dtype=bool)
        for p in primes[1:bisect_right(primes, target**.25)]:
            p = int(p)
            is_prime[(smallest_odd_multiple_of_n_geq_m(p, segment_min) - segment_min) // 2 :: p] = False
        new_primes = np.arange(segment_min, target**.5 + 1, 2, dtype=np.uint64)[is_prime]
        for div in new_primes:
            if target//div*div == target:
                target = target//div
                prime_divs.resize(len(prime_divs) + 1, refcheck=False)
                prime_divs[-1] = div

    for div in prime_divs:
        divs[div] = 1
    while target > 1 and old_target != target:
        old_target = target
        for div in prime_divs:
            if target//div*div == target:
                target = target//div
                divs[div] += 1
    if target != 1:
        divs[target] = 1

    return divs

def main():
    from time import time
    i = int(input('Inserire un numero: '))
    start = time()
    f = factorize(i)
    for n in f:
        n = int(n)
        if f[n] == 1:
            print(n)
        else:
            print(n, '^', f[n])
    print('Done in:', time() - start, 'seconds')

if __name__ == '__main__':
    main()