'''
Implementation of Quick Sort
06/25/2018
'''

def quickSort(arr):
	if not len(arr):
		return []
	else:
		quickSortInternal(arr, 0, len(arr) - 1)
		return arr

def quickSortInternal(arr, low, high):
	if low < high:
		pivot = (low + high) // 2
		pivot = partition(arr, low, high, pivot)
		quickSortInternal(arr, low, pivot - 1)
		quickSortInternal(arr, pivot + 1, high)


#caveat for two element arrays: 
#Since we use mid(floored) value as pivot point,
#we should not use switch arr[low] and arr[pivot], which causes pivot value not getting swapped
#we should swap arr[high] and arr[pivot], which guarantees a swap of element
def partition(arr, low, high, pivot):
	print("low: {}, high: {}, pivot: {}, arr: {}".format(low, high, pivot, arr))
	#swap pivot element with last element in the array
	arr[pivot], arr[high] = arr[high], arr[pivot]

	i = low
	j = high

	while i < j:

		#move left pointer
		while i < j and arr[i] <= arr[high]:
			i += 1

		#move right pointer
		while i < j and arr[j] >= arr[high]:
			j -= 1

		#swap out of order elements
		if i < j:
			arr[i], arr[j] = arr[j], arr[i]

	arr[i], arr[high] = arr[high], arr[i]

	return i

	#swap the elment in pivot position and low position
	# arr[low], arr[pivot] = arr[pivot], arr[low]

	# i = low
	# j = high

	# while i < j:
		
	# 	#move left pointer
	# 	while i < j and arr[i] <= arr[low]:
	# 		i += 1

	# 	#move right pointer
	# 	while i < j and arr[j] >= arr[low]:
	# 		j -= 1

	# 	#swap out of roder elements
	# 	if i < j:
	# 		arr[i], arr[j] = arr[j], arr[i]

	# 	print('i {}, j {}, arr: {}'.format(i, j, arr))

	# arr[low], arr[i-1] = arr[i-1], arr[low]

	# return i-1

if __name__ == "__main__":
	inputStr = input("Please input a list of integers separated by comma(,): ")
	inputList = [int(num) for num in inputStr.split(",")]
	print("The sorting result is {}".format(quickSort(inputList)))