'''
✔ Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
'''

# my_list = [1, 1, 22, 22, 5, 7, 10, 10]
# duplicate = []
#
# for item in my_list:
#     if my_list.count(item) > 1 and not item in duplicate:
#         duplicate.append(item)
# print(duplicate)

# import random
#
# lst = [random.randint(0, 10) for _ in range(20)]
# print(lst)
# duplicate = []
# for item in set(lst):
#     if lst.count(item) == 2: # != 1
#         duplicate.append(item)
# print(duplicate)


'''
✔ В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.
'''

# import re
# from collections import Counter
#
#
# def top_10_words(text):
#     words = re.findall(r'\b\w+\b', text.lower())
#     return Counter(words).most_common(10)
#
#
# text = ('''
#         Картина была представлена на многочисленных всесоюзных, всероссийских и международных выставках.
#         На Всемирной выставке 1958 года в Брюсселе Александр Дейнека за неё и другие представленные здесь работы
#         (панно советского павильона «За мир» и картины «Оборона Петрограда» и «Окраина Москвы. 1941 год»)
#         был награждён золотой медалью выставки.
#         Картина «Эстафета по кольцу „Б“» привлекала интерес советских и современных российских искусствоведов
#         (среди них академик Российской академии художеств, кандидат искусствоведения Владимир Сысоев,
#         кандидат искусствоведения Пётр Черёмушкин, доктор педагогических наук и член Союза художников
#         России Евгений Шорохов, художник-плакатист и литератор Нина Ватолина).
#         Подробно анализирует полотно в книге «Спорт в СССР.
#         Физическая культура — визуальная культура» (2010) доктор философии,
#         профессор Бристольского университета Майк О’Махоуни.
#         ''')
#
# print(top_10_words(text))

# Variant #2

# text = 'inviuerhkv vjieromvk joiemrocoe oerrjfierjoi  nforenmokf nmkomerokmcoi moe3rfm'
#
# words = []
# word = ''
#
# for ch in text.lower():
#     if ch.isalpha():
#         word += ch
#     else:
#         if word:
#             words.append(word)
#         word = ''
# else:
#     words.append(word)
#
# word_count = sorted([(words.count(word), word) for word in set(words)], reverse=True)
# for i in range(3):
#     print(f'{i+1}. {word_count[i][1]: <10} - {word_count[i][0]}')


'''
✔ Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
✔ *Верните все возможные варианты комплектации рюкзака.
'''
# def bag(items, max_weight):
#         possible_items = []
#         for item, weight in items.items():
#                 if weight <= max_weight:
#                         possible_items.append(item)
#                         max_weight -= weight
#         return possible_items
#
#
# items = {'water': 4, 'food': 2, 'eat': 3, 'clothes': 1, 'tent': 5}
# max_weight = 10
# print(bag(items, max_weight))

'''
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
 Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
'''

# friends = {
#     'Evgeniy': {'вода', 'фонарь', 'нож', 'еда'},
#     'Andrey': {'фонарь', 'еда', 'вода', 'нож'},
#     'Sergey': {'фонарь', 'вода', 'туалетная бумага', 'нож'},
# }
#
# # Находим вещи, которые взяли все три друга
#
# common_items = set(list(friends.values())[0])
# for friend, items in friends.items():
#     common_items &= items
# if common_items:
#     print('Вещи, которые взяли все друзья:', common_items)
# else:
#     print('Вещей, которые взяли все друзья - нет.')
#
# # Находим вещи, которые есть только у одного друга
#
# all_items = set()
# for friend, items in friends.items():
#     all_items |= items
# print(f'Вещи, которые есть только у одного друга: {all_items - common_items}')
#
# # Находим вещи, которые есть у всех, кроме одного
#
# items_without_one_friend = {}
# for friend, items in friends.items():
#     items_without_other_friends = items - common_items
#     items_without_one_friend[friend] = items_without_other_friends
#
# print('\nВещи, которые есть у всех, кроме одного:')
# for friend, items in items_without_one_friend.items():
#     print(f'{friend}: {items}')
