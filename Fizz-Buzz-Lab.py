def fizz_buzz(number):
	"""
	This function returns 'Fizz', 'Buzz', 'FizzBuzz', or the number passed to it
	depending on whether the number is divisible by, 3, 5, or both 3 and 5, respectively.
	"""
	if (number % 3 == 0) and (number % 5 == 0):
		return "FizzBuzz"
	elif number % 3 == 0:
		return "Fizz"
	elif number % 5 == 0:
		return "Buzz"
	else:
		return number