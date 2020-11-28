
count = count1 = doki = dokibukvi = 0
y = '1'

print('Введите пароль соответствующий требованиям \nтребования - хотя бы 1 цыфра и хотя бы 1 большая английская буква, а так же не меньше 8 символов\nА так же не больше 32 символов ')
while doki == 0 or dokibukvi == 0 or count < 8 or count > 32:
	x = input('Введите пароль')
	count = len(str(x))
	while count1 < count:
		S = x[count1: count1 + 1]
		countnn = S.isdigit()
		count1 += 1
		if str(countnn) == 'True':
			doki += 1
		if S == 'A' or S == 'B' or S == 'C' or S == 'D' or S == 'E' or S == 'F' or S == 'G' or S == 'H' or S == 'I' or S == 'J' or S == 'K' or S == 'L' or S == 'M' or S == 'N' or S == 'O' or S == 'P' or S == 'V' or S == 'R' or S == 'S' or S == 'T' or S == 'Q' or S == 'W' or S == 'X' or S == 'Z':
			dokibukvi += 1
	if doki == 0 or dokibukvi == 0 or count < 8 or count > 32:
		print('Пароль не соответствует требованиям')
		input('')
	print('Количество цыфр ', doki, '\nКоличество больших латинских букв', dokibukvi, '\nКоличество символов', count)
	input('')
	if dokibukvi > 0 and doki > 0 and count >= 8 and count <= 32:
		input('Пароль соответствует требованиям')
		while x != y:
			y = input('Введите пароль повторно')
			if x == y:
				print('Пароль верный')
			else:
				print('Пароль неверный')
input('')