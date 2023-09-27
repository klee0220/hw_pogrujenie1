'''
✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''

# def prime_num(x):
#     prs = {}
#     p = 1
#     while p < x:
#         if p not in prs:
#             yield p
#             prs[p * p] = [p]
#         else:
#             for s in prs[p]:
#                 prs.setdefault(s + p, []).append(s)
#             del prs[p]
#         p += 1
#
#
# print(*prime_num(50))
'''
✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''
# import os
#
#
# def main(user_path):
#     file_name = os.path.basename(user_path)
#     path_to_file = os.path.dirname(user_path)
#     file_extension = os.path.splitext(user_path)[1]
#     return (path_to_file, file_name, file_extension)
#
#
# if __name__ == '__main__':
#     # path_from_user = input('Enter an absolute path to file: ')
#     path_from_user = '/home/klee/PycharmProjects/task5.py'
#     print(main(user_path=path_from_user))


'''
✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
'''
# def main(names_list, rates_list, premium_list):
#     return {name: rate * (1 + float(prem.strip('%'))) for name, rate, prem in zip(names_list, rates_list, premium_list)}
#
#
# if __name__ == '__main__':
#     names = ['John', 'Kate', 'Gabriel']
#     rates = [0.5, 1, 1.5]
#     premium = ['11.15%', '12.25%', '13.35%']
#     print(main(names, rates, premium))

'''
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# if __name__ == '__main__':
#     number = int(input('Give amount: '))
#     print(list(fib(number)))