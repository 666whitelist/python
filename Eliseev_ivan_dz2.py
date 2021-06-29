"""
Выяснить тип результата выражений:

"""

mult = 15 * 3
print(isinstance(mult, int))
print(mult)

div = 15 / 3
print(isinstance(div, float))
print(div)

div_2 = 15 // 2
print(isinstance(div_2, int))
print(div_2)

mult_2 = 15**2
print(isinstance(mult_2, int))
print(mult_2)

"""
Необходимо обработать список
а) обособить каждое число кавычками(но не вещественные)
б) сформировать строку 
в) выявляем числа их строки
"""

data_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in range(1,8,2):
    data_list.insert(i, '"')
data_list.insert(-2, '"')
data_list.insert(-1, '"')

data_list[2] = '05'
data_list[-3] = '+05'

message = ' '.join(data_list)

print(message)

"""
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
"""

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
item_first = name_list[0] #сейчас будет много повторяющегося кода. Знаю, что можно сделать функцию, но ее еще не проходили
item_first = item_first.split(',')
for line in item_first:
    print('Привет,', line[20:31], '!')
item_second = name_list[1].title()
item_second = item_second.split(',')
for line in item_second:
    print('Привет,', line[18:31], '!')
item_third = name_list[2].title()
item_third = item_third.split(',')
for line in item_third:
    print('Привет,', line[23:31], '!')
item_fourth = name_list[3].title()
item_fourth = item_fourth.split(',')
for line in item_fourth:
    print('Привет,', line[9:31], '!')

"""
Создать вручную список, содержащий цены на товары (10–20 товаров)
"""
prices = [57.8, 46.01, 97, 43.6, 0.7, 25.4, 134.5, 53.68, 94.24, 35.35]
prices_all = ""

def get_formatted_price(price_local):
    price_parts_int_and_fractional = str(price_local).split(".")
    price_part_int = price_parts_int_and_fractional[0]
    price_parts_fractional = get_price_part_fractional(price_parts_int_and_fractional)
    return f'{price_part_int} руб {price_parts_fractional} коп'

def get_price_part_fractional(price_parts):
    if len(price_parts) == 1:
        return "00"
    if len(price_parts[1]) == 1:
        return f'0{price_parts[1]}'
    return price_parts[1]

for index, price in enumerate(prices):
    formatted_price = get_formatted_price(price)
    prefix = ""
    if index != 0:
        prefix =','

    prices_all += f'{prefix}{formatted_price}'

print(prices_all)




