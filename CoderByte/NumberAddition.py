def NumberAddition(str):
	"""
	Takes a string mixed with numbers, letters, punctuation, etc.
	Finds each number and adds them together to return a sum
	"""
	count = 0
	num = 0
	for c in str:
		if c.isdigit():
			num = num * 10 + int(c) # Move over 1 place
		else:
			count += num
			num = 0
	count += num # Adds any numbers that maybe remaining
	return count

print NumberAddition('75Number9') == 84
