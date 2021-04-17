def dicounted(price, discount, max_discount=50):
    # max_discount именованный элемент, указывать его необязательно,
    # если не указать то  то приймет заранее заданнное значение
    if type(price) != int:
        raise ValueError('Укажите цену цифрами')
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))

    if max_discount > 90:
        raise ValueError('Максимальная скидка не может быть больше 90%')
    # обработка исключений если выполняется условие то выводится ошибка
    # сообщение  указанное в raise
    if discount > max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount/100

    return price_with_discount


print(dicounted(500, 60, 75))
