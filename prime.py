primes = []

def isPrime(i):
    if i <= 1:
        return False
    elif i <= 3:
        if i not in primes:
            primes.append(i)
            return True
    elif i % 2 == 0 or i % 3 == 0:
        return False
    m = 5
    while m*m <= i:
        if i % m == 0 or i % (m + 2) == 0:
            return False
        m += 6
    primes.append(i)
    return True

import itertools

def PrimeChecker(num):
    num_arr = list(str(num))
    t = itertools.permutations(list(str(num)))
    k = [ int("".join(elm)) for elm in t ]
    k.sort()
    print k
    for i in k:
        if isPrime(i):
            return 1
    return 0

print PrimeChecker(30) == 1

def largest(n):
    if n == 0 or type(n) != int:
        return False
    list = range(10**n)
    for elm in sorted(list, reverse=True):
        largest = elm
        if isPrime(largest) == True:
            return elm

from math import sqrt

def primes(n):
    """
    Recursive function to calculate primes up to n.
    Incorporates fact that it is enought to examine multiples of the prime numbers up to sqrt(n)

    n: integer up to which we calculate primes

    Returns: set of prime numbers up to and including n if it's prime
    """
    if n == 0 or n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = { j for i in p for j in xrange(i*2, n+1, i) }
        p = { x for x in xrange(2, n + 1) if x not in no_p }
    return p

for i in range(1,50):
    print i, primes(i)
