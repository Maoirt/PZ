#1. Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
#Проверить истинность высказывания: «Треугольник со сторонами a, b, c является прямоугольным».
def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

valid_input = False

while not valid_input:
    try:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))

        if is_right_triangle(a, b, c):
            print("Треугольник со сторонами", a, ",", b, ",", c, "является прямоугольным.")
        else:
            print("Треугольник со сторонами", a, ",", b, ",", c, "не является прямоугольным.")
        
        valid_input = True

    except ValueError:
        # Обработка ошибки, если введены некорректные значения сторон треугольника
        print("Введите целые числа для сторон треугольника.")

    except TypeError:
        # Обработка ошибки, если аргументы не являются числами
        print("Введите числа для сторон треугольника.")

#2. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.

valid_input = False

while not valid_input:
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        c = int(input("Введите число c: "))

        minimum = min(a, b, c)
        maximum = max(a, b, c)

        print("Наименьшее число:", minimum)
        print("Наибольшее число:", maximum)
        
        valid_input = True

    except ValueError:
        # Обработка ошибки, если введены некорректные значения чисел
        print("Введите целые числа.")

    except TypeError:
        # Обработка ошибки, если аргументы не являются числами
        print("Введите числа.")