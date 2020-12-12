moneyall = money = 0
counter = counterfornumber = 0
memory = number = 0
numbercounter = 1


nachalo = kolvoosn = kolvo = int(input('Введите сколько человек в кругу'))

while kolvo != 0:
	number += numbercounter
	numbercounter += 1
	kolvo -= 1
kolvo = kolvoosn
print(number)


osnova = minus = int(input('Введите какой по счету будет выбывать человек'))
while kolvo > 1:
	while minus != 0:
		counter += 1
		minus -= 1
		money += 1
		counterfornumber += 1
		if counterfornumber == nachalo + 1:
			counterfornumber = 1
		if counter == kolvo + 1:
			counter = 1

	memory += counterfornumber
	nachalo -= 1

	if money <= kolvoosn:
		while money <= kolvoosn:
			money += 2
			kolvoosn += 1
	kolvo -= 1
	kolvoosn = kolvo
	moneyall += money
	money = 0
	minus = osnova
number -= memory
print('Всего у оставшегося номера', number, moneyall, 'монет')
print('Правильно работает только если счет меньше чем всего людей')
input('')