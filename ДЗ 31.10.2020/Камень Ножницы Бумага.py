print('Добро пожаловать в камень ножницы бумага, сдесь вы будете играть с ботом.\nВ конце игры вам покажут статистику, если хотите что бы она была точнее играйте больше.')
Game = int(input('Введите сколько игр играть будете '))
scissors = bumaga = kamen = raza = wins = 0
import random
for i in range (Game):
	input()
	BotChoice = random.randint(1, 3)
	YourChoice = int(input("Введите камень(1) бумага(2) или ножницы(3) "))
	print('Соперник выкинул', BotChoice)
	if YourChoice == 1 and BotChoice == 3:
		print("Вы победили ")
		wins += 1
	elif YourChoice == BotChoice + 1:
		print("Вы победили ")
		wins += 1
	elif YourChoice == BotChoice:
		print("Ничья ")
		x += 1
	else:
		print('Вы проиграли')
	raza += 1
	if YourChoice == 1:
		kamen += 1
	if YourChoice == 2:
		bumaga += 1
	if YourChoice == 3:
		scissors += 1

if kamen >= bumaga + scissors:
	print('Против вас ОЧЕНЬ эффективна бумага, ваш любимый выбор это камень')
elif bumaga >= kamen + scissors:
	print('Против вас ОЧЕНЬ эффективны ножницы, ваш любимый выбор это бумага')
elif scissors >= kamen + bumaga:
	print('Против вас ОЧЕНЬ эффективен камень, ваш любимый выбор это ножницы')
elif scissors > kamen and scissor > bumaga:
	print('Против вас довольно таки эффективен камень, ваш любимый выбор это ножницы')
elif kamen > scissors and kamen > bumaga:
	print('Против вас довольно таки эффективна бумага, ваш любимый выбор это камень')
elif bumaga > scissors and bumaga > kamen:
	print('Против вас довольно таки эффективны ножницы, ваш любимый выбор это бумага')
else:
	print('Вы играете сбалансированно')
print('Вы выиграли', wins, 'раз')
print('Вы выбрали камень', kamen, 'раз, бумагу', bumaga, 'раз, а ножницы', scissors, 'раз')
input('')