# 1. С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.

def draw_line(symbol, length):
    line = symbol * length
    return line

def draw_frame(word):
    horizontal_line = draw_line('-', len(word) + 4)
    vertical_line = draw_line('|', 1) + ' ' + word + ' ' + draw_line('|', 1)

    print(horizontal_line)
    print(vertical_line)
    print(horizontal_line)

#Пример заключения слово в рамку из линий
word = "Hello"
draw_frame(word)

# 2. Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C
# таким образом, чтобы их значения оказались упорядоченными по убыванию (A, B,
# C — вещественные параметры, являющиеся одновременно входными и
# выходными). С помощью этой функции упорядочить по убыванию два данных
# набора из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def SortDec3(A, B, C):
    if not isinstance(A, (float, int)) or not isinstance(B, (float, int)) or not isinstance(C, (float, int)):
        raise ValueError("Значения должны быть типа int или float ")
    
    if A < B:
        A, B = B, A
    if B < C:
        B, C = C, B
    if A < B:
        A, B = B, A
    return A, B, C

# Пример использования функции для упорядочивания двух наборов чисел
A1, B1, C1 = 5, 2, 8
A2, B2, C2 = 10, 1, 6

A1, B1, C1 = SortDec3(A1, B1, C1)
A2, B2, C2 = SortDec3(A2, B2, C2)

print(A1, B1, C1)
print(A2, B2, C2) 
