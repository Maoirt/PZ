# 1. Дан список размера N. Поменять местами его минимальный и максимальный
# элементы.

def swap_min_max(lst):
    try:
        if len(lst) == 0:
            raise ValueError("Лист пуст")

        min_idx = lst.index(min(lst))
        max_idx = lst.index(max(lst))

        # Меняем местами минимальный и максимальный элементы
        lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]

        return lst

    except ValueError as e:
        print(f"Error: {e}")
        return None

#Пример использования функции, которая меняет местами мин. и макс. элементы
print(swap_min_max([9,2,6,4]))


# 2. Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент BK равен сумме элементов списка A с номерами от K
# до N.


def generate_list_b(lst):
    try:
        if len(lst) == 0:
            raise ValueError("Лист пуст")

        n = len(lst)
        list_b = []

        for k in range(n):
            sum_elements = sum(lst[k:])  # Исправлено: от k до конца списка
            list_b.append(sum_elements)

        return list_b

    except ValueError as e:
        print(f"Error: {e}")
        return None

# Пример использования
print(generate_list_b([9, 2, 6, 4]))

# 3. Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).

def cyclic_shift(lst):
    try:
        if len(lst) == 0:
            raise ValueError("Лист пуст")

        last_element = lst.pop()  # Удаляем последний элемент списка
        lst.insert(0, last_element)  # Вставляем его в начало списка

        return lst

    except ValueError as e:
        print(f"Error: {e}")
        return None
#Пример использования функции
print(cyclic_shift([9,2,6,4]))
