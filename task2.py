'''
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''


# card_cash = 0
#
#
# def push_cash(card_cash, a):
#     if a % 50 != 0:
#         return (f'Summa popolneniya == 50 y.e., na schetu - {card_cash}')
#     else:
#         card_cash += a
#     print(f'Schet popolnen na :{a}, balans  = {card_cash}')
#     return card_cash
#
#
# def get_cash(card_cash, b):
#     if b % 50 != 0:
#         return (f'Summa snyatiya ne menee 50 y.e., na schetu - {card_cash}')
#     elif b % 50 == 0:
#         if 30 <= b * 0.015 <= 600:
#             print(f'So scheta shyali :{b + (b * 0.015)}, balans  = {card_cash - b + (b * 0.015)}')
#             return card_cash - b - (b * 0.015)
#         elif b * 0.015 < 30:
#             print(f'So scheta shyali :{b + 30}, balans  = {card_cash - (b + 30)}')
#             return card_cash - (b + 30)
#         else:
#             print(f'So scheta shyali :{b + 600}, balans  = {card_cash - (b + 600) }')
#             return card_cash- (b + 600)
# print(get_cash(100, 50))
#
#
# def bonus(card_cash, counter):
#     if counter == 3:
#         card_cash *= 1.03
#         print(f'Vam nachislen bonus 3% {card_cash}')
#         return card_cash
#     return card_cash
#
#
# def millionare(card_cash):
#     if card_cash >= 5000000:
#         card_cash -= 0.1 * card_cash
#         print(f'Nalog 10% = {card_cash}')
#         return card_cash
#     return card_cash
#
#
# counter = 0
# while True:
#     insert_card = int(input(f'Menu:\n 1. Popolnenie balansa:\n 2. Snyatie sredstv:\n 3. Vernut katrtu:'))
#     if insert_card == 1:
#         a = int(input('Vvedite summu popolneniya - '))
#         card_cash = push_cash(card_cash, a)
#         counter += 1
#         card_cash = bonus(card_cash, counter)
#         card_cash = millionare(card_cash)
#     elif insert_card == 2:
#         a = int(input('Vvedite summu snyatiya - '))
#         card_cash = get_cash(card_cash, a)
#         counter += 1
#         card_cash = bonus(card_cash, counter)
#         card_cash = millionare(card_cash)
#     elif insert_card == 3:
#         print(card_cash)
#         break










'''
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
'''

# a = int(input('Input number: '))
#
# def my_hex(a):
#     hexadecimal_digits = "0123456789ABCDEF"  # Строка с шестнадцатеричными цифрами
#     hexadecimal_number = ""
#
#     while a > 0:
#         remainder = a % 16  # Получаем остаток от деления на 16
#         hexadecimal_digit = hexadecimal_digits[remainder]  # Получаем шестнадцатеричную цифру
#         hexadecimal_number = hexadecimal_digit + hexadecimal_number  # Добавляем цифру в начало шестнадцатеричного числа
#         a //= 16  # Выполняем целочисленное деление на 16
#
#     return hexadecimal_number
#
# print(my_hex(a))


'''
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
'''

# from fractions import Fraction



# a = list(map(int, input('input a: ').split('/')))
# b = list(map(int, input('input b: ').split('/')))
#
#
#
# def lcm(a, b):
#     m = a * b
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return m // (a + b)
#
#
# def nod(lst):
#     a = lst[0]
#     b = lst[-1]
#     while a != 0 and b != 0:
#         if a >= b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
#
#
#
# # summa
# if a [-1] == b[-1]:
#     summa = [a[0] + b[0], a[-1]]
# else:
#     nod1 = lcm(a[-1], b[-1])
#     summa = [a[0] * nod1 // a[-1] + b[0] * nod1 // b[-1], nod1]
# # proizvedenie
# mult = [a[0]*b[-1], b[0]*a[-1]]
#
#
# nodsum = nod(summa)
# nodmult = nod(mult)
#
# summa = [summa[0] // nodsum, summa[-1] // nodsum]
# mult = [mult[0] // nodmult, mult[-1] // nodmult]
#
# print("/".join([str(i) for i in summa]), "/".join([str(i) for i in mult]))


# 3/4 + 2/5 = 3*5 + 2*4 / 5*4
# 3/4 * 2/5 = 3*5 /4*2
