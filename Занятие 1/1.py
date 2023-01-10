"""
1.	Вывести на экран список пар «ID студента — возраст».
2.	Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов всех студентов и общую длину всех фамилий студентов.
3.	Далее в основном коде эта функция вызывается, и значения присваиваются отдельным переменным, которые после выводятся на экран. (Т.е. нужно распаковать все возвращаемые значения в отдельные переменные.)
"""

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']

    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt

# 1
pairs = []
for i in students:
    pairs += (i, students[i]['age'])

print(pairs)


my_lst = f(students)[0]
l = f(students)[1]

print(my_lst, l)
