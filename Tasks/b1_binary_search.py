from typing import Any, Sequence, Optional
import numpy as np

def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	print(elem, arr)
	return None

def min_elem(find_elem, arr):
	index = None
	find_elem = np.random.choice(array)
	left = 0
	right = len(arr) - 1
	middle = (left + right) // 2

	while True:
		if find_elem == middle:
			index = find_elem
			return index
		else:
			if find_elem < middle:
				right = middle - 1
			else:
				left = middle + 1


if __name__ == "__main__":
	n = 10
	array = np.arange(n)
	find_elem = np.random.choice(array)
	np.random.shuffle(array)
	print(min_elem(find_elem, array))
