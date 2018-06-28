class Node:
	def __init__(self, value = 0, nextLink = None):
		self.value = value
		self.next = nextLink

	def __str__(self):
		return str(self.value)

class ListQueue:
	def __init__(self, firstLink = None, lastLink = None):
		self.firstLink = firstLink
		self.lastLink = lastLink

	def addBackListQueue(self, newValue = 0):
		newNode = Node(newValue)

		if self.isEmptyListQueue():
			self.firstLink = self.lastLink = newNode
		else:
			self.lastLink.next = newNode
			self.lastLink = newNode

	def frontListQueue(self):
		if self.firstLink != None:
			return self.firstLink.value
		else:
			return None

	def removeFrontListQueue(self):
		if self.isEmptyListQueue():
			return
		elif self.firstLink == self.lastLink:
			self.firstLink = self.lastLink = None
		else:
			self.firstLink = self.firstLink.next

	def isEmptyListQueue(self):
		return self.firstLink == None and self.lastLink == None

	def __str__(self):
		node = self.firstLink
		returnStr = ''
		while True:
			if node != None:
				returnStr += str(node.value) + ' '
				node = node.next
			else:
				break

		return returnStr

class ListDeque(ListQueue):
	def addFrontListQueue(self, newValue = 0):
		newNode = Node(newValue)
		if self.isEmptyListQueue():
			self.firstLink = self.lastLink = newNode
		else:
			newNode.next = self.firstLink
			self.firstLink = newNode

	def backListQueue(self):
		if self.lastLink != None:
			return self.lastLink.value
		else:
			return None

	def removeBackListQueue(self):
		if self.isEmptyListQueue():
			return
		elif self.firstLink == self.lastLink:
			self.firstLink = self.lastLink = None
		else:
			node = self.firstLink
			while node.next.next != None:
				node = node.next

			node.next = None
			self.lastLink = node

if __name__ == "__main__":
	#Queue
	q = ListQueue()
	q.addBackListQueue(4)
	q.addBackListQueue(5)
	q.addBackListQueue(6)
	q.addBackListQueue(7)
	q.removeFrontListQueue()
	q.removeFrontListQueue()
	q.removeFrontListQueue()
	print("Queue {}, FirstLink {}, LastLink {}".format(q, q.firstLink, q.lastLink))

	#Deque
	dq = ListDeque()
	dq.addFrontListQueue(2)
	dq.addFrontListQueue(1)
	dq.addBackListQueue(3)
	dq.removeFrontListQueue()
	dq.removeBackListQueue()
	print("Deque {}, FirstLink {}, LastLink {}".format(dq, dq.firstLink, dq.lastLink))