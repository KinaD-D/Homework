x = int(input("Введите число, и вам выдатут простое ли оно "))
if x == 2 or x == 3 or x == 5 or x == 7:
	print('Это число простое')
elif x == 1:
	print('Не простое')
elif x / 2 != x // 2 and x / 3 != x // 3 and x / 5 != x // 5 and x / 7 != x // 7:
	print('Это простое число')

else:
	print('Это  не простое число')
input()