import random
input('В этой программе вам создадут случайное кол-во чисел от 0 до 2, все они будут равнятся 12\nВ конце вам покажут среднее кол-во двоек, не 0ей а так же среднее колво чисел')
x = kolvo1All = kolvo2All = kolvo0 = kolvo1 = kolvo2 = 0
kolvoAll = 0
for i in range (20):
	print ('\nВсего цифр было', kolvo0 + kolvo1 + kolvo2, '\nНулей было', kolvo0, 'Едениц', kolvo1, 'Двоек', kolvo2, '\n')
	kolvoAll = kolvoAll + kolvo0 + kolvo1 + kolvo2
	x = kolvo0 = kolvo1 = kolvo2 = 0
	while x != 12:
		b = random.randint(0, 2)
		if b == 0:
			kolvo0 += 1
		if b == 1:
			x += 1
			kolvo1 += 1
			kolvo1All += 1
		if b == 2:
			kolvo2 += 1
			kolvo2All += 1
			x += 2
		if x != 13:
			print(b)
		else:
			x = x - b
print('В среднем выходило', kolvo2All // 20, 'Двоек')
print('В среднем выходило примерно ', kolvoAll // 20,' чисел')
print('Не нулевых значений в среднем было ', (kolvo2All + kolvo1All) // 20 )
input()