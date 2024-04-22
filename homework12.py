def test(discount, *price, txt='Сумма товаров:', **products):
    summ = 0
    for i in range(len(price)):
        if price[i] >= 1000:
            summ += price[i] - price[i] / 100 * discount
        else:
            summ += price[i]
    print(txt, summ)
    for key, product in products.items():
        print(key, product)


test(10, 2000, 200, 900, txt='Сумма товаров со скидкой:', book=2000, pen=200)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print()
print(factorial(6))