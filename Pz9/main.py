# Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее
# значение роста (в см.). (Пример, {"Андрей": 178, "Виктор": 150, "Максим": 200, …},
# наибольшее 200, наименьшее 150)

def calculate_average_age(persons_dict):
    try:
        if not persons_dict:  # Проверка на пустой словарь
            raise ValueError("Словарь пуст")
        
        total_age = 0
        count = 0
        
        for age in persons_dict.values():
            total_age += age
            count += 1
        
        average_age = total_age / count
        return average_age
    
    except ValueError as e:
        print(f"Ошибка: {e}")

# Пример
persons = {"Андрей": 32, "Виктор": 29, "Максим": 18}
average_age = calculate_average_age(persons)
print(f"Средний возраст: {average_age:.2f}")

