class Node:
	def __init__(self, value = 0, prev = None, nextNode = None):
		self.value = value
		self.prev = prev
		self.next = nextNode	

class BagLinkedList:
	def __init__(self, front = None, back = None):
		self.size = 0
		self.frontSentinel = front
		self.backSentinel = back

		!!frontSentinel and backSentinel also needs to be a Node!!

	def _addBefore(self, node = None, value = 0):
		if node != None:
			newNode = Node(value, node.prev, node)
			node.prev.next = newNode
			node.prev = newNode

	def _removeLink(self, node = None):
		if node != None:
			node.prev.next = node.next
			node.next.prev = node.prev

	def addLinkedList(self, value = 0):
		if self.frontSentinel == None and self.backSentinel == None:
			newNode = Node(value, self.frontSentinel, self.backSentinel)
			self.frontSentinel = newNode
			self.backSentinel = newNode
		else:
			self._addBefore(self.frontSentinel, value)
