def elevator_distance(array):
	total = 0

	for i in range(1, len(array), 2):
		total += abs(array[i] - array[i - 1])
		if len(array) - 1 >= i + 1:
			total += abs(array[i] - array[i + 1])
	return total


print(elevator_distance([1, 2, 3]))
