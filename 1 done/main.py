str = input('Введите строку: ')

def first_symbol(str):
    if (str[0] == ')') or (str[0] == ']') or (str[0] == '}'):   # если строка начинается на запрещённый символ
        print('Строки не существует')                           # её 100% не существует
        exit()

def order_of_bracket(str):
    if (str.find('(}') > 0) or (str.find('(]') > 0) or (str.find('[}') > 0) or \
        (str.find('{)') > 0) or (str.find('[)') > 0) or (str.find('{]') > 0):
        print('Строки не существует')                           # её 100% не существует
        exit()

    while len(str) != 0:    # пока длина строки не станет равной нулю
                            # будем вырезать из неё "комплект" скобок
        first_symbol(str)   # опять проверка первого символа
        open_symbol = str[0]                   # запоминаем открывающую скобку типа X
        str = str.replace(open_symbol, '', 1)  # удаляем её из строки

        if open_symbol == '(':                  # если открывающая скобка типа "(" 
            closed_symbol = str.find(')')       # то ищем закрывающую типа ")"
            if not closed_symbol != -1:         # если закрывающей скобки в строке нет
                print('Строки не существует')   # её не существует
                exit()
            str = str.replace(str[closed_symbol], '', 1)    # удаляем зыкрывающую скобку из строки
        # в следующих двух блоках повторяется логика первого блока, только для "{}" и "[]"
        if open_symbol == '[':
            closed_symbol = str.find(']')
            if not closed_symbol != -1:
                print('Строки не существует')
                exit()
            str = str.replace(str[closed_symbol], '', 1)

        if open_symbol == '{':
            closed_symbol = str.find('}')
            if not closed_symbol != -1:
                print('Строки не существует')
                exit()
            str = str.replace(str[closed_symbol], '', 1)

print('Строка существует')
