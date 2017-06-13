def permutation_palindrome(s):
	l = list(s)
	count = {}
	for c in l:
		if c in count:
			count[c] += 1
		else:
			count[c] = 1

	number_of_odds = 0
	for v in count.values():
		# v is odd
		if (v % 2):
			number_of_odds += 1
		if number_of_odds > 1:
			return False
	return True


def has_palindrome_permutation(the_string):
	# track characters we've seen an odd number of times
	unpaired_characters = set()

	for char in the_string:
		if char in unpaired_characters:
			unpaired_characters.remove(char)
		else:
			unpaired_characters.add(char)

	# the string has a palindrome permutation if it
	# has one or zero characters without a pair
	return len(unpaired_characters) <= 1

print permutation_palindrome("civic")
print permutation_palindrome("ivicc")
print permutation_palindrome("civil")
print permutation_palindrome("livci")
print has_palindrome_permutation("civic")
