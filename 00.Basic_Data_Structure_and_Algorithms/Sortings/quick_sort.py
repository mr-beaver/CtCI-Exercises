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
	if low >= high:
		return
	else:
		pivot = (low + high) // 2
		pivot = partition(arr, low, high, pivot)
		quickSortInternal(arr, low, pivot - 1)
		quickSortInternal(arr, pivot + 1, high)

def partition(arr, low, high, pivot):
	#swap the elment in pivot position and low position
	arr[low], arr[pivot] = arr[pivot], arr[low]

	i = low + 1
	j = high

	while i < j:
		if arr[i] <= arr[low]:
			i += 1
		elif arr[j] >= arr[low]:
			j -= 1
		else:
			arr[i], arr[j] = arr[j], arr[i]

	#swap back pivot, new j should be at the top of first section
	arr[low], arr[j] = arr[j], arr[low]

	print("low: {}, high: {}, pivot: {}, arr: {}".format(low, high, pivot, arr))

	return j

if __name__ == "__main__":
	inputStr = input("Please input a list of integers separated by comma(,): ")
	inputList = [int(num) for num in inputStr.split(",")]
	print("The sorting result is {}".format(quickSort(inputList)))