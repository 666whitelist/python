
"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

"""


1 минута = 60 сек
1 час = 60 минут
1 день = 24 часа


for i in range(5):
    user_time = int(input('Введите кол-во секунд:'))
    sec = user_time % 60  # находим секунды как остаток
    min = user_time // 60  # находим минуты
    hour = user_time // 3600  # находим часы(в одном часе 3600 сек)
    days = user_time // 86400  # находим дни(в одном дне 86400 сек)

    if user_time < 60:
        print(f'{user_time} сек')
    elif user_time >= 60 and user_time < 3600:
        print(f'{min} мин {sec} сек')
    elif user_time >= 3600 and user_time < 86400:
        print(f'{hour} час {min - (hour * 60)} мин {sec} сек')
    elif user_time >= 86400:
        print(f'{days} дн {hour - (days * 24)} час {min - (hour * 60) } мин {sec} сек')

"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
* Решить задачу под пунктом b, не создавая новый список.
"""

numbers = []
numbers = list(range(1, 1000, 2))
for number in numbers:
    if number % 7 == 0:
        number = str(number)
        number = list(number)
        print(number)
        # numbers.append(number)



"""
Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
"""

user_number = int(input('Введите число от 1 до 20'))

if user_number == 1 :
    print(f'{user_number} процент')
elif user_number >= 2 and user_number <= 4:
    print(f'{user_number} процента')
else:
    print(f'{user_number} процентов')



