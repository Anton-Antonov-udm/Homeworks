#                      Фабрика функций для сложения и вычитания:

def create_operation(operation):
    if operation == 'add':
        def add(x, y):
            return x + y
        return add # возвращаем функцию как объект!! Тут скобки не нужны
    elif operation == 'sub':
        def sub(x, y):
            return x - y
        return sub
    elif operation == 'mul':
        def mul(x, y):
            return x * y
        return mul
    elif operation == 'div':
        def div(x, y):
            if y == 0:
                return 'На ноль делить нельзя'
                # raise Exception('На ноль делить нельзя')
            else:
                return x / y
        return div


my_func = create_operation('add')
print(my_func(5,2))
my_func = create_operation('sub')
print(my_func(10,4))
my_func = create_operation('mul')
print(my_func(5,3))
my_func = create_operation('div')
print(my_func(1,2))
print(my_func(11,0))


#                      Пример лямбда функции с аналогом через def

number = int(input('Введите число: '))
num_degree = int(input('Возвести в степень: '))
result = lambda x, y: x ** y

print('Результьат лямбда функции: ', result(number, num_degree))


def number_degree(x, y):
    return x ** y


print('Результат стандартной функции: ', result(number, num_degree))


#                      Пример создания вызываемого объекта

class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect_1 = Rect(5, 4)
print(rect_1.__call__())

rect_1 = Rect(3, 6)
print(rect_1.__call__())
