def is_prime(func):
    def inner(*args):
        value = func(*args)
        for i in range(value):
            if value > i > 1:
                while value % i != 0:
                    print('Число простое')
                    break
                else:
                    print('Число составное')
                    break
                break
        return func
    return inner


@is_prime
def sum_three(num_1, num_2, num_3):
    return num_1 + num_2 + num_3


result = sum_three(2, 3, 6)
print(result)
