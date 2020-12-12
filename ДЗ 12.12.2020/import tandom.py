import random
maxcount = countcount = 0
input('Они будут создаваться пока там не будет 3 повторяющихся числа')
while countcount != 3:
	somelist = []
	for i in range(random.randint(5, 200)):
		somelist += [random.randint(1, 100)]
	somelist = sorted(somelist)
	nachalo = somelist
	print(somelist)
	for j in range(len(nachalo)):
		jx = somelist[j - 1]
		count = nachalo.count(jx)
		if count == 3:
			countcount = 3
			maxcount = jx
print('Самое максимальное повторяющиеся 3 раза число это', maxcount, '\nИх сумма равна', int(maxcount) * 3)
input('')

count = j = 0
for j in range(len(somelist)):
	if count < somelist.count(somelist[int(j) - 1]):
		countcount = somelist[int(j) - 1]
		count = somelist.count(somelist[int(j) - 1])
print('Самое часто повторяющиеся число это', countcount, 'оно повторяется', count, 'раз')
input('')

count = 0

print('Сейчас вам покажут Самое большое число (нечетное и которое делится на 3)')
for i in range(len(somelist)):
	if somelist[i] % 3 == 0 and somelist[i] % 2 == 1:
		count = somelist[i]
print('Самое максимальное число =', count, '\nОно делится на 3 и нечетное')
input('')
