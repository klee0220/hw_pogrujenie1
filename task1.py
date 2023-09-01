'''
1.Выведите в консоль таблицу умножения от
2х2 до 9х10 как на школьной тетрадке.
'''
# for i in range(2, 10):
#     for j in range(2, 11):
#         print(i, 'x', j, '=', i*j)
#     print('')

'''
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого 
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше 
суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является 
ли треугольник разносторонним, равнобедренным или равносторонним.
'''

# a, b, c = input('Input number: ').split()
#
#
# def check_triangle(a, b, c):
#     if a <= b + c or b <= a + c or c <= a + b:
#         return 'It is not triangle'
#     elif a > b + c or b > a + c or c > a + b:
#         return 'Triangle is scalene'
#     elif a == b == c:
#         return 'Triangle is equilateral'
#     elif a == b or a == c or b == c:
#         return 'Triangle is isosceles'
# print(check_triangle(a, b, c))
#

'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''
#
# a = int(input('Input number:'))
#
# def check_number(a):
#     n = 2
#     if a < 0 or a > 100000:
#         return 'Error try again!'
#     while a % n != 0:
#         n += 1
#         return f'{n == a} This is a prime number'
#     else:
#         return 'This is composite number'
# print(check_number(a))

'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код:

from random import
randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

n = input('Input number: ')


def random(lower_limit, upper_limit):
    lower_limit = 0
    upper_limit = 1000
    comp_num = random(lower_limit, upper_limit)
    att = 1
    while lower_limit != upper_limit:
        print(f'Ваше число равно, больше или меньше:, {comp_num}')
        z = input()
        if 'больше' in z.lower():
            lower_limit = comp_num
            comp_num = random(lower_limit, upper_limit)
            att += 1
        elif 'меньше' in z.lower():
            upper_limit = comp_num
            comp_num = random(lower_limit, upper_limit)
            att += 1
        elif 'равно' in z.lower():
            break
print(f'Ваше число:{n} ,а число найденное компьютером: {comp_num},кол-во попыток: {att}')






