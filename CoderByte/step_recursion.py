memo = {1:1,2:2} # Base cases added initially
# Use Memoization to keep track of ways possible for each num of steps

def climb_steps(n):
	"""
	Recursivly finds number of possible ways to climb n steps

	n: number of steps
	"""
	# Base Case
	if n in memo:
		return memo[n]
	else:
		ways = climb_steps(n-1) + climb_steps(n-2)
		memo[n] = ways
		return ways

print climb_steps(4) == 5
print climb_steps(6) == 13
