'''
Implementation of converting infix format to postfix format

06/20/2018: 
	1. assume all the operands are single character
	2. assume all the parentheses are in the form of "(" and ")"
	3. assume all input is a string and it is all legit

'''

#import Stack class from stack
from stack import Stack

#function for converting Infix to Postfix
def infix_to_prefix(infixStr = ''):
	
	#operators collection
	operators = ['+', '-', '*', '/']
	#initialize a new stack
	s = Stack()
	#initialize result postfix string
	result = ''

	for c in infixStr.replace(' ', ''):
		if c.isalpha():
			#append to the result string directly
			result += c

		elif c in operators:
			
			#stack is not empty, compare
			if not s.isEmpty(): 
				
				#check operator order 
				result += returnHigherPrecedence(s, c)
				
				#push it into the stack
				s.push(c)

			#stack is empty push directly
			else:
				s.push(c)

		else:

			#opening parentheses, push to the top
			if c == '(':
				s.push(c)
			#closing parentheses, pop stack until there is an opening parentheses
			else:
				while s.top() != '(':
					result += s.pop()

				s.pop() #pop the opening parentheses
	
	while not s.isEmpty():
		result += s.pop()

	return result

#check higher precedence operators in stack for current stack
def returnHigherPrecedence(st, current):
	ret = ''
	# + and -
	if current == '+' or current == '-':
		while not st.isEmpty() and st.top() != '(':
			ret += st.pop()

	# * and /
	if current == '*' or current == '/':
		while not st.isEmpty() and (st.top() == '*' or st.top() == '/'):
			ret += st.pop()

	return ret


if __name__ == "__main__":
	infixStr = input('Enter infix string: ')
	print(infix_to_prefix(infixStr))

