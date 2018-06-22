'''
Implementation of checking palindrome using two stacks
06/21/2018
'''

import math
from stack import Stack

def checkPalindrome(string):
	s1 = Stack()
	s2 = Stack()
	count = 1
	result = True

	for c in string:
		s1.push(c)

	while count <= math.floor(len(string) / 2):
		s2.push(s1.pop())
		count += 1

	if len(string) % 2 == 1:
		s1.pop()

	while not s1.isEmpty():
		if s1.pop() != s2.pop():
			result = False
			break;

	return result

if __name__ == "__main__":
	inputString = input('Please input a string: ')
	print("Palindrome, {}".format(checkPalindrome(inputString)))