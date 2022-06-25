class Stack:
	def __init__(self):
		self.items = []
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:
				return self.items.pop()
		except IndexError:
				print("Stack is empty")
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		return self.__len__() == 0

# pseudo code
def parChecker(parSeq):
	S = Stack()
	for symbol in parSeq:
		if symbol in "({[":
			S.push(symbol)
		elif symbol in ")]}":
			if S.isEmpty():
				return False
			if ord(S.top()) + 1 <= ord(symbol) <= ord(S.top()) + 2:
				S.pop()
			else:
				return False
	if S.isEmpty():
		return True
	else:
		return False
	
k = parChecker(input())
print(k)