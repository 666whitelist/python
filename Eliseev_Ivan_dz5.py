"""
Задание номер 1
"""
import random

def odd_nums(nums: int):
    for _ in range(1, nums, 2):
        yield _

odd_to_10 = odd_nums(10)

print(next(odd_to_10))
print(next(odd_to_10))

"""
Задание 1 *
"""

odd_nums_short = (x for x in range(10) if x % 2 == 1)
print(next(odd_nums_short))
print(next(odd_nums_short))
print(next(odd_nums_short))

"""
Задание 3
"""
from itertools import islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
tutors_data = ((i, j) if i != j else None for j in klasses for i in tutors )
print(*islice(tutors_data, 7))
# tutors_set = set(tutors)
# klasses_set = set(klasses)
# def tutors_data(tutors, klasses):
#     for name in tutors:
#         for clas in klasses:
#             yield (tutors, klasses)
#
# tut_data = tutors_data(tutors_set, klasses_set)
# print(next(tut_data))
# print(*zip(tutors, klasses))

# tutors_data = []
#
# for name in tutors:
#     for clas in klasses:
#         tutors_data.append(name +' '+ clas)
# print(tutors_data)