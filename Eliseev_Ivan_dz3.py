"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
"""

def num_translator(keys):
    all_list = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    values = all_list.get(keys)
    if keys == keys.title():
        print(values.title()) #не знаю как победить ошибку NoneType при title
    else: print(values)


num_translator('Zero')

"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки
"""

# def thesarurs(*names):
    letter_dict = {}
    for name in names:
        sort_by_letter = name[0]
        if sort_by_letter not in letter_dict:
            letter_dict[sort_by_letter] = []
        letter_dict[sort_by_letter].append(name)
    print(letter_dict)
    return letter_dict


thesarurs('Mike', 'Leo', 'Kate', 'Kevin')

"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
"""
import random

def get_jokes(quantaty):
    for i in range(quantaty):
        random_nouns = random.choice(nouns)
        random_adverbs = random.choice(adverbs)
        random_adjectives = random.choice(adjectives)
        print(random_nouns, random_adverbs, random_adjectives)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(4)