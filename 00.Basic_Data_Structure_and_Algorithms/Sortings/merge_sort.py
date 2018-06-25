'''
Implementation of Merge Sort
06/24/2018

Do NOT return an array every time and then combine them.
Use an empty and write the result into it to save space complexity.
'''

def mergeSort(arr):
	if not len(arr):
		return []
	else:
		result = [0] * len(arr)
		split(arr, 0, len(arr) - 1, result)
		return arr

def split(arr, low, high, result):
	#single element, return do not change anything
	if low >= high:
		return
	#multiple element, continue
	else:
		mid = (low + high) // 2
		split(arr, low, mid, result)
		split(arr, mid + 1, high, result)
		merge(arr, low, mid, high, result)

		for i in range(low, high + 1):
			arr[i] = result[i]

	print("low: {}, high: {}, result: {}".format(low, high, result))

def merge(arr, low, mid, high, result):
	i = low
	j = mid + 1
	count = low	

	while i <= mid and j <= high:
		if arr[i] < arr[j]:
			result[count] = arr[i]
			i += 1
		else:
			result[count] = arr[j]
			j += 1
		count += 1

	while i <= mid:
		result[count] = arr[i]
		count += 1
		i += 1

	while j <= high:
		result[count] = arr[j]
		count += 1
		j += 1


if __name__ == "__main__":
	inputList = input('Please enter a list of integers separated by comma(,): ')
	arr = [int(num) for num in inputList.split(',')]
	print("The sorted result is {}".format(mergeSort(arr)))