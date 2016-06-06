# Write a function, `letter_count(str)` that takes a string and
# returns a hash mapping each letter to its frequency. Do not include
# spaces.
#
# Difficulty: 1/5

def letter_count(str):
	h = {}
	word_arr = str.split()
	for word in word_arr:
		for char in word:
			h[char] = h.get(char,0) + 1
	return h

print "Tests for letter counts in string"
print letter_count('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print letter_count("cats are fun") == {'a': 2, 'c': 1, 'e': 1, 'f': 1, 'n': 1, 's': 1, 'r': 1, 'u': 1, 't': 1}
print "===================================="

# Write a function, `nearest_larger(arr, i)` which takes an array and an
# index.  The function should return another index, `j`: this should
# satisfy:
#
# (a) `arr[i] < arr[j]`, AND
# (b) there is no `j2` closer to `i` than `j` where `arr[i] < arr[j2]`.
#
# In case of ties (see example below), choose the earliest (left-most)
# of the two indices. If no number in `arr` is larger than `arr[i]`,
# return `nil`.
#
# Difficulty: 2/5

def nearest_larger(arr, idx):
	diff = 1
	for i in range(len(arr)-1):
		right = idx+diff
		left = idx-diff
		if (left >= 0) and (arr[left] > arr[idx]):
			return left
		elif (right < len(arr)) and (arr[right] > arr[idx]):
			return right
		diff += 1

print "Tests for nearest larger int in arr"
print nearest_larger([2,3,4,8], 2) == 3
print nearest_larger([2,8,4,3], 2) == 1
print nearest_larger([2,6,4,8], 2) == 1
print nearest_larger([2,6,4,6], 2) == 1
print nearest_larger([8,2,4,3], 2) == 0
print nearest_larger([2,4,3,8], 1) == 3
print nearest_larger([2, 6, 4, 8], 3) == None
print nearest_larger([2, 6, 9, 4, 8], 3) == 2
print "================================"


# Build a function, `morse_encode(str)` that takes in a string (no
# numbers or punctuation) and outputs the morse code for it. See
# http://en.wikipedia.org/wiki/Morse_code. Put two spaces between
# words and one space between letters.
#
# You'll have to type in morse code: I'd use a hash to map letters to
# codes. Don't worry about numbers.
#
# I wrote a helper method `morse_encode_word(word)` that handled a
# single word.
#
# Difficulty: 2/5

CODE = {'A': '.-',	 'B': '-...',   'C': '-.-.',
		'D': '-..',	'E': '.',	  'F': '..-.',
		'G': '--.',	'H': '....',   'I': '..',
		'J': '.---',   'K': '-.-',	'L': '.-..',
		'M': '--',	 'N': '-.',	 'O': '---',
		'P': '.--.',   'Q': '--.-',   'R': '.-.',
		'S': '...',	'T': '-',	  'U': '..-',
		'V': '...-',   'W': '.--',	'X': '-..-',
		'Y': '-.--',   'Z': '--..'}

# CODE found on internet

def morse_encode(str):
	 word_arr = str.split()
	 morse_arr = [ morse_encode_word(word) for word in word_arr ]
	 return "  ".join(morse_arr).strip()

def morse_encode_word(word):
	letters = list(word) # Pythonic way to split word into letters
	code = [ CODE[letter.upper()] for letter in letters ]
	return " ".join(code)

print "Test for morse encode"
print morse_encode("cat") == "-.-. .- -"
print morse_encode("cat in hat")  == "-.-. .- -  .. -.  .... .- -"
print "====================================="
# Catsylvanian money is a strange thing: they have a coin for every
# denomination (including zero!). A wonky change machine in
# Catsylvania takes any coin of value N and returns 3 new coins,
# valued at N/2, N/3 and N/4 (rounding down).
#
# Write a method `wonky_coins(n)` that returns the number of coins you
# are left with if you take all non-zero coins and keep feeding them
# back into the machine until you are left with only zero-value coins.
#
# Difficulty: 3/5

def wonky_coins(n):
	if n == 0:
		return 1
	else:
		return wonky_coins(n/4) + wonky_coins(n/3) + wonky_coins(n/2)

print "Test for wonky coins"
print wonky_coins(1) == 3
print wonky_coins(5) == 11
print wonky_coins(6) == 15
print wonky_coins(0) == 1
print "===================================="

# Write a function word_unscrambler that takes two inputs: a scrambled
# word and a dictionary of real words.  Your program must then output
# all words that our scrambled word can unscramble to.
#
# Hint: To see if a string `s1` is an anagram of `s2`, split both
# strings into arrays of letters. Sort the two arrays. If they are
# equal, then they are anagrams.
#
# Difficulty: 3/5

def word_unscrambler(word, dictionary):
	anagrams = []
	s1 = sorted(list(word))
	for elm in dictionary:
		s2 = sorted(list(elm))
		if s1 == s2:
			anagrams.append(elm)
	return anagrams

print "Test for word unscrambler"
print word_unscrambler("cat", ["tac"]) == ["tac"]
print word_unscrambler("cat", ["tom"]) == []
print word_unscrambler("cat", ["tic", "toc", "tac", "toe"]) == ["tac"]
print word_unscrambler("cat", ["scatter", "tac", "ca"] ) == ["tac"]
print word_unscrambler("turn", ["numb", "turn", "runt", "nurt"]) == ["turn", "runt", "nurt"]
print "================================="

# Write a function, `rec_intersection(rect1, rect2)` and returns the
# intersection of the two.
#
# Rectangles are represented as a pair of coordinate-pairs: the
# bottom-left and top-right coordinates (given in `[x, y]` notation).
#
# Hint: You can calculate the left-most x coordinate of the
# intersection by taking the maximum of the left-most x coordinate of
# each rectangle. Likewise, you can calculate the top-most y
# coordinate of the intersection by taking the minimum of the top most
# y coordinate of each rectangle.
#
# Difficulty: 4/5

def rec_intersection(rect1, rect2):

	x_min = max(rect1[0][0],rect2[0][0])
	x_max = min(rect1[1][0],rect2[1][0])

	y_min = max(rect1[0][1],rect2[0][1])
	y_max = min(rect1[1][1],rect2[1][1])

	if x_min > x_max or y_min > y_max:
		return None
	else:
		return [[x_min,y_min],[x_max,y_max]]

print "Test for rec intersection"
print rec_intersection([[0, 0], [2, 1]], [[1, 0], [3, 1]]) == [[1, 0], [2, 1]]
print rec_intersection([[1, 1], [2, 2]], [[0, 0], [5, 5]]) == [[1, 1], [2, 2]]
print rec_intersection([[1, 1], [2, 2]], [[4, 4], [5, 5]]) == None
print rec_intersection([[1, 1], [5, 4]], [[2, 2], [3, 5]]) == [[2, 2], [3, 4]]
print "==============================================="

# Write a function `bubble_sort(arr)` which will sort an array of
# integers using the "bubble sort"
# methodology. (http://en.wikipedia.org/wiki/Bubble_sort)
#
# Difficulty: 3/5

def bubble_sort(arr):
	while True:
		swaps = 0
		for i in range(len(arr)-1):
			if arr[i+1] < arr[i]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
				swaps += 1
		if swaps == 0:
			break
	return arr

print "Tests for bubble sort"
print bubble_sort([]) == []
print bubble_sort([1]) == [1]
print bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
print "==============================================="

# Write a method, `ordered_vowel_words(str)` that takes a string of
# lowercase words and returns a string with just the words containing
# all their vowels (excluding "y") in alphabetical order. Vowels may
# be repeated (`"afoot"` is an ordered vowel word).
#
# You will probably want a helper method, `ordered_vowel_word?(word)`
# which returns true/false if a word's vowels are ordered.
#
# Difficulty: 2/5

def ordered_vowel_words(str):
	ordered_words = ""
	for word in str.split():
		if ordered_vowel_word(word):
			ordered_words += word + " "
	return ordered_words.strip()

def ordered_vowel_word(word):
	vowels = 'aeiou'
	last_vowel = None
	for char in word:
		if char in vowels:
			if char >= last_vowel:
				last_vowel = char
			else:
				return False
	return True

print "Tests for ordered vowel words"
print ordered_vowel_words("amends") == "amends"
print ordered_vowel_words("complicated") == ""
print ordered_vowel_words("afoot") == "afoot"
print ordered_vowel_words("ham") == "ham"
print ordered_vowel_words("crypt") == "crypt"
print ordered_vowel_words("o") == "o"
print ordered_vowel_words("tamely") == "tamely"
phrase = "this is a test of the vowel ordering system"
result = "this is a test of the system"
print ordered_vowel_words(phrase) == result
