def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        temp = num / i
        if temp.is_integer() and i != num:
            return False
    return True


def filter_function(iter_object):
    list_objects = []

    if type(iter_object) is dict:
        for key in iter_object:
            if is_prime(key) is True:
                list_objects.append(iter_object[key])
    else:
        for i in range(len(iter_object)):
            if is_prime(i) is True:
                list_objects.append(iter_object[i])
    return list_objects


def get_filter_list(temp_object):
    return filter_function(temp_object)


# a = [i for i in range(100)]
b = {1: 0, 2: 1, 3: 1, 4: 0, 6: 0}

a = [1, 2, 5, 3, 3]
c = (1, 2, 3, 4)
s = 'abcd'


print('Словарь: ', get_filter_list(b))
print('Список: ', get_filter_list(a))
print('Строка: ', get_filter_list(s))

