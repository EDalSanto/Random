def isprime(n):
    """Returns True if n is prime using AKS"""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def calc_primes(m,n):
    primes = [i for i in range(m,n+1) if isprime(i)==True]
    return primes

def gap(g, m, n):
    primes = calc_primes(m,n)
    for index,prime in enumerate(primes):
    # compare prime to each subsequent prime up until the dif is greater than g then start at next prime
        for prime2 in primes[index+1:]:
            if prime2 - prime == g and prime2 == primes[index+1]:
                return [prime, prime2]
            elif prime2 - prime > g:
                break
    return None
