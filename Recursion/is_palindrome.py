# simple version
def is_palindrome(str):
	if len(str) <= 1:
		return True
	else:
		if str[0] != str[len(str) - 1]:
			return False
	return is_palindrome(str[1:len(str) - 1])


print is_palindrome("toto")
print is_palindrome("rotor")


# helper version
def is_palindrome_(string):
	# scope
	res = True

	def slice(start, end):
		if start == end:
			return
		if string[start] != string[end]:
			res = False
			return res
		else:
			slice(start + 1, end - 1)

	slice(0, len(string) - 1)
	return res


print is_palindrome("toto")
print is_palindrome("rotor")
