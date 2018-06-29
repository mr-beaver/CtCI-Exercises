class Bag:
	def __init__(self, newList = None):
		if newList != None:
			self.bag = newList
		else:
			self.bag = []

	def add(self, newValue):
		if newValue != None:
			self.bag.append(newValue)
		return self.bag

	def remove(self, value):
		self.bag = [x for x in self.bag if x != value]

	def contains(self, value):
		return not not self.bag.count(value)

	def size(self):
		return len(self.bag)

	def __str__(self):
		return str(self.bag)

if __name__ == "__main__":
	bag = Bag()
	bag.add(4)
	bag.add(4)
	bag.add(4)
	bag.add(5)
	print("Bag contains 4 is {}".format(bag.contains(4)))
	bag.remove(4)
	print("Bag contains 4 is {}".format(bag.contains(4)))	
	print(bag)