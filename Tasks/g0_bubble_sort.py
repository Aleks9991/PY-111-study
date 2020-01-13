from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	container

	replace = 0
	for i in range(len(container) - 1):
		for j in range(len(container) - 1 - i):
			if container[j] > container[j+1]:
				container[j], container[j + 1] = container[j + 1], container[j]
                replace += 1
                print('Count replace', replace)
                replace = 0
                return container

if __name__ == '__main__':
    import random
    N = 5
    # shuffle_list = list(range(N))
    # random.shuffle(shuffle_list)
    shuffle_list = [4, 3, 2, 1, 0]
    # shuffle_list = [1, 0, 4, 2, 3]
    # shuffle_list = [0, 1, 2, 4, 5]
    print(sort(shuffle_list))
