x = input('Введдите символы, а все что между /* и */ исключат, вводить границы можно несколько раз')
while x.find('/*') != -1 or x.find('*/') != -1:
	finder1 = x.find('/*')
	finder2 = x.find('*/')
	deliter = x[finder1: finder2 + 2]
	x = x.replace(deliter, '')
	print(deliter)
	print(x)
input()