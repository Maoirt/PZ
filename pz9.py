# Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее
# значение роста (в см.). (Пример, {"Андрей": 178, "Виктор": 150, "Максим": 200, …},
# наибольшее 200, наименьшее 150)

def find_min_max_height(persons):
    if not persons:
        raise ValueError("Словарь пуст")

    min_height = 999
    max_height = -999

    for person, height in persons.items():
        if height < min_height:
            min_height = height
        if height > max_height:
            max_height = height

    return min_height, max_height

try:
    dictionary = {"Андрей": 178, "Виктор": 150, "Максим": 200}  # пример словаря
    min_height, max_height = find_min_max_height(dictionary)
    print("Наименьшее значение роста:", min_height)
    print("Наибольшее значение роста:", max_height)
except Exception as e:
    print("Error:", {e})

