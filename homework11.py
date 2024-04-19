def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a=True, b=1, c='строка')
#print_params('white', 77, 78, False)
print_params(True, 1)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['yellow', 55, True]
values_dict = {'a': 'blue', 'b': [43, 34], 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[12, 21], 'green']

print_params(*values_list_2, 42)
