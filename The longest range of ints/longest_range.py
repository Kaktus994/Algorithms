def longest_range(array):

	if len(array) == 1:
		return [array[0]]*2

	array = list(set(array))
	array.sort()
	new_dict = {}
	start_element = None
	
	for i, element in enumerate(array):
		if i == len(array)-1:
			break

		if array[i+1] == element + 1:
			if start_element == None:
				start_element = array[i]

		elif start_element != None:
			new_dict[start_element] = [start_element, element]
			start_element = None

	if i == len(array) - 1 and start_element:
		new_dict[start_element] = [start_element, element]

	if not new_dict:
		new_dict[0] = array

	return max(new_dict.items(), key=lambda x: x[1][1] - x[1][0])[1]


"""
Test
"""
if __name__ == "__main__":

	array = [7, 6, 4, 3, 8]
	array_1 = [1, 7, 3, 3, -1, 8, 9, 0, 10, 2, 6, -10, -9, -8, -7, -6]
	array_2 = [1, 2, -3, 4, 5]
	array_3 = [5]

	print(longest_range(array))
