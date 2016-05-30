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


def largest(n):
    if n == 0 or type(n) != int:
        return False
    list = range(10**n)
    for elm in sorted(list, reverse=True):
        largest = elm
        if isPrime(largest) == True:
            return elm
