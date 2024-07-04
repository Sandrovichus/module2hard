print('Программа для генерации древнего шифра')
print('______________________________________')
while True:
    result = ''
    n = int(input('Введите любое число от 3 до 20: '))
    if n > 20 or n < 3:
        print('Введите число в правильном диапазоне - от 3 до 20!')
        continue
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result = result + str(i) + str(j)
    print(f'Шифр для числа {n}: {result}')
