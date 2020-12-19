import random

class SetofStack:
	def __init__(self):
		self._stack = []

	def add(self, adder):			#Тут добавляется элемент
		self._stack.append(adder)
		return adder

	def take(self, taker):			#Тут показывается и убирается
		try:
			return self._stack.pop(taker)
		except IndexError:
			return "\nЭто не должно выводиться"

	def counter(self):				#Показывает количество элементов
		return len(self._stack)


class Stack:
	def __init__(self):
		self._stack = []

	def add(self, maxkolvo, kolvo, count, list):
		count = 0
		list = []
		if kolvo >= maxkolvo:
			while count != maxkolvo:
				count += 1
				list += str(count)
			return list
		elif kolvo != 0:
			while kolvo != 0:
				count += 1
				list += str(count)
				kolvo -= 1
			return list
SetofStack = SetofStack()
Stack = Stack()


list = []
chel = 0
count = 0
maxi = int(input('Введите сколько тарелок может быть в стопке '))
kolvo = int(input('Введите сколько тарелок вы хотите разложить '))

if kolvo >= maxi:
	while  kolvo >= maxi:
		print('Первая стопка состоит из', SetofStack.add(Stack.add(maxi, kolvo, chel, list)), 'тарелок')
		kolvo -= maxi
		count += 1
if kolvo != 0:
	print('Первая стопка состоит из', SetofStack.add(Stack.add(maxi, kolvo, chel, list)), 'тарелок')
	count += 1
print('Получилось всего', SetofStack.counter(), 'Стопок из тарелок')
	
for x in range(count):
	print('Вы помыли', SetofStack.take(chel))
input()
