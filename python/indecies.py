def get_indecies(element):
	array = [1, 6, 4, 7, 8, 3, 6]
	indecies = []
	for i in range(len(array)):
		if array[i] == element:
			indecies.append(i)
	else:
		return indecies



print(get_indecies(6))
