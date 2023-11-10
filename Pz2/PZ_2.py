# k = int(input("Введите номер дня в году (от 1 до 365): "))
# weekday = (k + 5) % 7
# print("Номер дня недели:", weekday if weekday != 0 else 7)

#Дни недели пронумерованы следующим образом: 1 — понедельник,
#2 — вторник, ..., 6 — суббота, 7 — воскресенье. Дано целое число K, лежащее в диапазоне
#1-365. Определить номер дня недели для K-го дня года, если известно, что в этом году 1
#января было субботой.

try:
    # Запросить у пользователя номер дня в году
    k = int(input("Введите номер дня в году (от 1 до 365): "))
    
    # Проверить, что введенное значение находится в диапазоне от 1 до 365
    if k < 1 or k > 365:
        raise ValueError("Ошибка: введите целое число от 1 до 365.")
    
    # Вычислить номер дня недели
    weekday = (k + 5) % 7
    
    # Вывести результат
    print("Номер дня недели:", weekday if weekday != 0 else 7)
    
except ValueError as e:
    # Обработать исключение, если пользователь ввел некорректное значение
    print(e)

    