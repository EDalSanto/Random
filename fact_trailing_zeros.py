facts = {}
def factorial(n):
    if n in facts:
        return facts[n]
    elif len(facts) == 0:
        result = 1
        for i in xrange(2,n+1):
            result *= i
            facts[i] = result
        return result
    else:
        temp = facts[max(facts)]
        for i in xrange(max(facts), n+1):
            temp *= i
            facts[i] = temp
        return temp


def zeros(n):
    zeros = 0
    fact = factorial(n)
    for num in str(fact)[::-1]:
        if num == '0':
            zeros += 1
        else:
            break
    return zeros
