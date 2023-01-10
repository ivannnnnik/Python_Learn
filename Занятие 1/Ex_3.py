

tuple_val = ('1', '9', ',', '2', '3', '4', '5', '2', '4', '3', ',', '5')
element = input()


def filter_func(temp_tuple, temp_value):
    start_index = -1
    end_index = -1

    if temp_tuple.count(temp_value) == 0:
        return ()

    if temp_tuple.count(temp_value) == 1:
        index_el = tuple_val.index(temp_value)
        return temp_tuple[index_el:]

    for i in range(len(temp_tuple)):
        if temp_tuple[i] == temp_value:
            if start_index == -1:
                start_index = i
            end_index = i

    return temp_tuple[start_index:end_index + 1]


print(filter_func(tuple_val, element))
