import random

class Stack:
	def __init__(self):
		self._stack = []

	def add(self, adder):
		self._stack.append(adder)

	def take(self, taker):
		try:
			return self._stack.pop(taker)
		except IndexError:
			return "\nЭто не должно выводиться"

	def counter(self):
		return len(self._stack)

someline = Stack()
chel = count = 0
for i in range(random.randint(10, 50)):
	count += 1
	someline.add(random.randint(1, 99))
print('Всего в очередь встало', someline.counter(), 'человек')
print('Первый в очереди на данный момент человек под номером', someline.take(1))
for a in range(count - 1):
	print('А следующий под номером', someline.take(chel))
print('Он же и последний')
input('')