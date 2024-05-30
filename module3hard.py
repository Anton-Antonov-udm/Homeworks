data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(values):
    sum_ = 0
    for i in values:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            sum_ += calculate_structure_sum(i)
        else:
            sum_ += calculate_structure_sum(list(i.items()))
    return sum_


print(calculate_structure_sum(data_structure))
