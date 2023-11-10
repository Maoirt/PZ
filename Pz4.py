#1. Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
#целые степени числа A от 1 до N.

while True:
    try:
        A = float(input("Введите вещественное число A: "))
        N = int(input("Введите целое число N (> 0): "))

        if N <= 0:
            raise ValueError("Число N должно быть больше 0.")

        # Выводим все целые степени числа A от 1 до N
        for i in range(1, N+1):
            result = A ** i
            print(f"{A} в степени {i} = {result}")

        break

    except ValueError as e:
        print(f"Ошибка: {e}")

        

#2. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
#деления, найти количество и сумму его цифр.

while True:
    try:
        N = int(input("Введите целое число N (> 0): "))

        if N <= 0:
            raise ValueError("Число N должно быть больше 0.")

        # Находим количество и сумму цифр числа N
        num = N
        count = 0
        total_sum = 0

        while num > 0:
            digit = num % 10
            count += 1
            total_sum += digit
            num //= 10

        print(f"Количество цифр в числе: {count}")
        print(f"Сумма цифр в числе: {total_sum}")

        break

    except ValueError as e:
        print(f"Ошибка: {e}")