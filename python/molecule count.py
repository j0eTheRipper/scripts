def separate(string):
	"""Separtates the string by integers"""
	result = []
	element = string[0]

	for char in string[1::]:
		if char.isalpha():
			if element.isdigit():
				result.append(int(element))
				element = char
			elif element.isupper() and char.islower():
				element += char
			else:
				result.append(element)
				element = char
		else:
			if element.isalpha():
				result.append(element)
				element = char
			else:
				element += char
	else:
		result.append(element if not element.isdigit() else int(element))

	return result


def break_grouping(symbol, equation):
	result = ''
	in_grouping = ''

	for i in equation:
		if i != symbol:
			result += i
		else:
			


def interpret_count(molecules):
	result = {}
	for i in range(len(molecules) - 1):
		current = molecules[i]
		upcoming = molecules[i + 1]
		if type(current) == str:
			if result.get(current):
				if type(upcoming) == int:
					result[current] += upcoming
				else:
					result[current] += 1
			else:
				if type(upcoming) == int:
					result[current] = upcoming
				else:
					result[current] = 1

	return result


x = separate('Mg2H2OCO2')
print(interpret_count(x))
