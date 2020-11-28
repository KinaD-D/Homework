count = 0
deleted = ''
osnova = x = str(input('Введите что зашифровать, если количество символов нечетное, оставшеяся символ допишется в конце '))
y = int(len(x))
c = len(x) // 2
x = osnova[c: len(osnova)]
y = osnova[0: c]

while count < len(osnova) // 2:
	countx = x[count]
	county = y[count]
	deleted += county + countx
	count += 1

if count < len(x) + 1:
	deleted += x[count]

print('Вот готовый шифр ', deleted)
input()