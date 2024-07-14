# class EvenNumbers:
#     def __init__(self, start=0, end=1):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             while self.start % 2 != 0:
#                 self.start += 1
#             result = self.start
#             self.start += 2
#             return result
#         else:
#             raise StopIteration
#
#
# en = EvenNumbers(10, 25)
# for i in en:
#     print(i)


class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            if self.step > 0 and self.pointer <= self.stop:
                result = self.pointer
                self.pointer += self.step
                return result
            if self.step < 0 and self.pointer >= self.stop:
                result = self.pointer
                self.pointer += self.step
                return result
            else:
                raise StopIteration()





try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()


