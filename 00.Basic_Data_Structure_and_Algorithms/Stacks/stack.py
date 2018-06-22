class Stack:
	def __init__(self, newList = None):
		if newList is None:
			self.stack = []
		else:
			self.stack = newList

	def pop(self):
		if len(self.stack):
			return self.stack.pop()

	def push(self, newVal = 0):
		self.stack.append(newVal)
		return self.stack

	def top(self):
		if len(self.stack):
			return self.stack[-1]
		else:
			return None

	def isEmpty(self):
		return not len(self.stack)

	def __str__(self):
		return str(self.stack)
