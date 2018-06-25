'''
Implementation of Queue and Deque using array
06/24/2018
'''
class Queue:
	def __init__(self, newList = None):
		if newList == None:
			self.queue = []
		else:
			self.queue = newList

	def addBack(self, newElement = None):
		if newElement != None:
			self.queue.append(newElement)
		return self.queue

	def front(self):
		return self.queue[0]

	def removeFront(self):
		self.queue = self.queue[1:]
		return self.queue

	def isEmpty(self):
		return not len(self.queue)

	def __str__(self):
		return str(self.queue)

	def __repr__(self):
		return str(self.queue)

class Deque(Queue):
	def addFront(self, newElement = None):
		if newElement != None:
			self.queue = [newElement] + self.queue
		return self.queue

	def back(self):
		return self.queue[-1]

	def removeBack(self):
		self.queue = self.queue[:-1]
		return self.queue