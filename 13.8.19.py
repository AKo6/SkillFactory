print("Спасибо, что решили посетить нашу онлайн-конференцию!\n"
      "При покупке более 3-х билетов будет скидка 10%")
print("---")
tickets = int(input("Укажите количество билетов:"))
if tickets <= 0:
    raise ValueError("Количество билетов не может быть отрицательным или нулём")
if tickets == 1:
    user_age = int(input("Укажите ваш возраст:"))
    if user_age > 80 or user_age <= 0:
        raise ValueError("Вам не может быть столько лет")
    if 18 <= user_age < 25:
        price = 990
    elif user_age < 18:
        price = 0
    else:
        price = 1390
    print("---")
    total = tickets * price
    if tickets > 3:
        total -= int((total * 10) / 100)
    if tickets != 1:
        print(f"Стоимость билетов составит: {total} рублей")
    else:
        print(f"Стоимость билета составит: {total} рублей")
elif tickets > 1:
    users_age = list(map(int, input("Укажите через пробел возраст посетителей: ").split()))
    while tickets != len(users_age):
        users_age = list(map(int, input("Вы не указали возраст всех посетителей.\n"
                                       " Укажите через пробел возраст посетителей: ").split()))
    price = []
    for i in users_age:
        if i in range(0,18):
            price.append(0)
        elif i in range(18,25):
            price.append(990)
        else:
            price.append(1390)
    if tickets > 3:
        discount = (sum(price) / 100) * 10
        total = sum(price) - discount
        print(f"Стоимость билетов составит: {total} рублей с учетом скидки: {discount}")
    else:
        total = sum(price)
        print(f"Стоимость билетов составит: {total} рублей")