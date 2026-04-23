import math
import random


def is_valid(num, size):
    return 1 <= num <= size


def is_valid_command(command):
    return command.lower() == 'да' or command.lower() == 'нет'


def guesser(len1, n):
    counter = 0
    fact_counter = math.ceil(math.log(len1, 2))
    while True:
        num = int(input(f'Введите число от 1 до {len1}: '))
        if not is_valid(num, len1):
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            if num < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
            elif num > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
            elif num == n:
                counter += 1
                print('Вы угадали, поздравляем!')
                print(f'Вы использовали {counter} попыток а максимум можно было за {fact_counter}')
                break


len1 = int(input('Укажите последнее число: '))
n = random.randint(1, len1)
print('Добро пожаловать в числовую угадайку')
guesser(len1, n)
while True:
    print('Хотите еще?: ')
    command = input('Да или Нет: ')
    if not is_valid_command(command):
        print('Только да или нет')
    elif command.lower() == 'да':
        len2 = int(input('Укажите последнее число: '))
        n2 = random.randint(1, len2)
        print('Добро пожаловать в числовую угадайку')
        guesser(len2, n2)
    else:
        command.lower() == 'нет'
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
