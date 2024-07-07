
print('Привет, в этом файле мы будем работать с прайс-листом')
print()

print('Для того чтобы вывести все содержимое файла нажмите 1 и Enter')
print()

user_input = input('Введите 1')


if user_input == 1:
	line = open('price.txt' , 'r')
	line1 = file.read()
	print(line1)

else:
	print('By!')
	


