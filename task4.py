'''
Напишите функцию для транспонирования матрицы
'''
matrica = [[2, 7, 4], [3, 6, 9], [1, 5, 8]]
trans_matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def trans_matrix(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            trans_matr[j][i] = matrica[i][j]
    return trans_matr


print(trans_matrix(matrica))

'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''

def asdzzxxz(**kwargs):
    a = {}
    kwargs.items()
    for i, v in kwargs.items():
        a[str(v)] = i
    return a


print(asdzzxxz(szszszs=1212, fcfcfcfg=2112))



'''
Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

card_cash = 0
MIN_CASH_TAX = 30
MAX_CASH_TAX = 600
ATM_PER = 0.015
GET_PUSH_MIN = 50


def push_cash(card_cash, a):
    if a % GET_PUSH_MIN != 0:
        return (f'Summa popolneniya == 50 y.e., na schetu - {card_cash}')
    else:
        card_cash += a
    print(f'Schet popolnen na :{a}, balans  = {card_cash}')
    return card_cash


def get_cash(card_cash, b):
    if b % GET_PUSH_MIN != 0:
        return (f'Summa snyatiya ne menee 50 y.e., na schetu - {card_cash}')
    elif b % GET_PUSH_MIN == 0:
        if MIN_CASH_TAX <= b * ATM_PER <= MAX_CASH_TAX:
            print(f'So scheta shyali :{b + (b * ATM_PER)}, balans  = {card_cash - b + (b * ATM_PER)}')
            return card_cash - b - (b * ATM_PER)
        elif b * ATM_PER < MIN_CASH_TAX:
            print(f'So scheta shyali :{b + MIN_CASH_TAX}, balans  = {card_cash - (b + MIN_CASH_TAX)}')
            return card_cash - (b + MIN_CASH_TAX)
        else:
            print(f'So scheta shyali :{b + MAX_CASH_TAX}, balans  = {card_cash - (b + MAX_CASH_TAX) }')
            return card_cash- (b + MAX_CASH_TAX)
print(get_cash(100, 50))


def bonus(card_cash, counter):
    if counter == 3:
        card_cash *= 1.03
        print(f'Vam nachislen bonus 3% {card_cash}')
        return card_cash
    return card_cash


def millionare(card_cash):
    if card_cash >= 5000000:
        card_cash -= 0.1 * card_cash
        print(f'Nalog 10% = {card_cash}')
        return card_cash
    return card_cash


counter = 0
while True:
    insert_card = int(input(f'Menu:\n 1. Popolnenie balansa:\n 2. Snyatie sredstv:\n 3. Vernut katrtu:'))
    if insert_card == 1:
        a = int(input('Vvedite summu popolneniya - '))
        card_cash = push_cash(card_cash, a)
        counter += 1
        card_cash = bonus(card_cash, counter)
        card_cash = millionare(card_cash)
    elif insert_card == 2:
        a = int(input('Vvedite summu snyatiya - '))
        card_cash = get_cash(card_cash, a)
        counter += 1
        card_cash = bonus(card_cash, counter)
        card_cash = millionare(card_cash)
    elif insert_card == 3:
        print(card_cash)
        break