from math import sqrt

def sieves(n):
	nums = [2] + range(3,n+1,2) # Exclude even numbers(can't be prime) except 2
	n_sqrt = int(sqrt(n))
	if n_sqrt % 2 == 0: # Possible that sqrt will be even, which we exlcuded from our potential primes list
		n_sqrt -= 1 # In that case, subtract 1
	sqrt_idx = nums.index(n_sqrt) # Find index
	for j in nums[:sqrt_idx+1]: # Iterate up to sqrt(n)
		p = j
		for i in range(p*2,n+1,p): # Remove multiples
			if i in nums: # Haven't already removed it
				nums.remove(i)
	return nums

print sieves(30)
