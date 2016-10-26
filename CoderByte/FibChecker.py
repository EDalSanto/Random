memo = {0:1,1:1}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result

def FibonacciChecker(num):
    i = 2
    while max(memo.values()) < num:
        fib(i)
        i += 1
    if num in memo.values():
        return 'yes'
    return 'no'
