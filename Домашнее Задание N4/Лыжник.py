c = x = 10
b = y = 1
n = int(input('Изначально лыжник пробежал 10 км \nс каждым днём он ехал на 10% больше \nBведите за сколько дней посчитать путь '))
while y < n + 11:
	x = x + (x / 10)
	if y < 10:
		print ('В', y + 1, 'день, он пробежал', x, 'км')
	y = y + 1
	c = c + x
	if y == n:
		print('В', n, 'день он всего прошёл', c, 'км')
	if y == 7:
		print('В первые 7 дней он прошёл', c, 'км')
	if c > 80 and b == 1:
		print('Что бы общее расстояние лыжника не привышало 80 ка ему нужно проходить', y - 1, 'дней')
		b += 1
input()