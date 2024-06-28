def square_root(value):
    return value ** 2


def is_odd(value):
    return value % 2


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result_1 = map(square_root, filter(is_odd, my_list))
print(result_1)
print(list(result_1))

result_2 = list(map(square_root, filter(is_odd, my_list)))
print(result_2)

