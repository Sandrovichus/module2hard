print('Программа для генерации древнего шифра')
print('______________________________________')
while True:
    result = ''
    number = int(input('Введите любое число от 3 до 20: '))
    if number > 20 or number < 3:
        print('Введите число в правильном диапазоне - от 3 до 20!')
        continue
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                result = result + str(i) + str(j)
    print(f'Шифр для числа {number}: {result}')
