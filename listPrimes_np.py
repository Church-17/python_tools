import numpy as np
from bisect import bisect_right

def list_prime(target: int) -> np.ndarray:
    smallest_odd_multiple_of_n_geq_m: int = lambda n, m : m + (n-m) % (2*n)
    primes = np.array([2, 3, 5, 7], dtype=np.uint64)
    index_segment_max = 3
    extend = 7
    segment_min, segment_max = 9, 49

    while segment_max < target:
        is_prime = np.full(shape=(segment_max-segment_min)//2, fill_value=True, dtype=bool)
        for p in primes[1:index_segment_max]:
            p = int(p)
            is_prime[(smallest_odd_multiple_of_n_geq_m(p, segment_min) - segment_min) // 2 :: p] = False
        new_primes = np.arange(segment_min, segment_max, 2, dtype=np.uint64)[is_prime]
        old_len = len(primes)
        primes.resize(old_len + len(new_primes))
        primes[old_len:] = new_primes
        index_segment_max += extend
        segment_min, segment_max = segment_max, int(primes[index_segment_max]) ** 2

    is_prime = np.full(shape=(target-segment_min+3)//2, fill_value=True, dtype=bool)
    for p in primes[1:bisect_right(primes, target**.5)]:
        p = int(p)
        is_prime[(smallest_odd_multiple_of_n_geq_m(p, segment_min) - segment_min) // 2 :: p] = False
    new_primes = np.arange(segment_min, target+2, 2, dtype=np.uint64)[is_prime]
    old_len = len(primes)
    primes.resize(old_len + len(new_primes))
    primes[old_len:] = new_primes

    return primes

def main():
    from time import time
    target = 10**9
    start = time()
    out = list_prime(target)
    elapsed = time() - start
    print(len(out))
    print('Done in: ', elapsed, 'seconds')

if __name__ == '__main__':
    main()