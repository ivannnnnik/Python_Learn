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
# Задание 1.1

# # 1
list_id_age = []
for key in students:
    list_id_age.append(key)
    list_id_age.append(students[key]['age'])
print(list_id_age)

# # 2
list_id_age = [(key, students[key]['age']) for key in students]
print(list_id_age)


# Задание 1.2

# # 1
def hobby_and_len_surname_1(students_dict):
    list_hobby_students = []
    len_all_surname_students = 0

    for key in students_dict:
        list_hobby_students += students_dict[key]['interests']
        len_all_surname_students += len(students_dict[key]['surname'])

    return list_hobby_students, len_all_surname_students


# # 2
def hobby_and_len_surname_2(students_dict):
    list_hobby_students = []
    for key in students_dict:
        list_hobby_students += students_dict[key]['interests']

    len_all_surname_students = sum([len(students_dict[key]['surname']) for key in students])
    return list_hobby_students, len_all_surname_students


result_func_1 = hobby_and_len_surname_1(students)
result_1_list, result_1_len = result_func_1[0], result_func_1[1]

print(result_1_list, result_1_len)


