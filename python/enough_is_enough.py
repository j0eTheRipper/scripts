def get_indecies(array, wanted_element):
    indecies = []
    for i in range(len(array)):
        if array[i] == wanted_element:
            indecies.append(i)
    else:
        return indecies

print(get_indecies([1, 2, 6, 3, 4,2, 45,3, 2, 2, 6,2], 2))