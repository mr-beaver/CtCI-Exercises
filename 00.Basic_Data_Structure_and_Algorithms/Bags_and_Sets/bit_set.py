'''
Implementation for 64bit bit set for 0 ~ 255 integers
07/04/2018
'''

class BitSet:
	def __init__(self, newSet = None):
		if newSet != None:
			self.store = newSet
		else:
			self.store = [0b0] * 4

	def bitsetSet(self, num):
		self.store[self.bitSetIndex(num)] |= self.bitSetMask(num)

	def bitsetGet(self, num):
		return bool(self.store[self.bitSetIndex(num)] & self.bitSetMask(num))

	def bitsetClear(self, num):
		self.store[self.bitSetIndex(num)] &= self.bitSetMask(num) ^ 63

	def __str__(self):
		return str(["{0:b}".format(x) for x in self.store])

	@staticmethod
	def bitSetIndex(num):
		return num // 64;

	@staticmethod
	def bitSetMask(num):
		return 0b1 << (num % 64)

if __name__ == "__main__":
	bs = BitSet()
	bs.bitsetSet(1)
	bs.bitsetSet(2)
	print(bs)
	print(bs.bitsetGet(0))
	bs.bitsetClear(1)
	print(bs)