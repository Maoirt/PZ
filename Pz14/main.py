#Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
#количество полученных элементов.

import re

# Чтение данных из файла experience.txt
with open('experience.tx', 'r', encoding='utf-8') as file:
  data = file.read()

# Поиск стажа работы сотрудников с использованием регулярных выражений
experience_pattern = r'(\d+ (?:год|года|лет).*)'
experiences = re.findall(experience_pattern, data)

# Подсчет количества найденных элементов
num_experience = len(experiences)

# Вывод результата
print("Найденые стажи работы:")
for exp in experiences:
  print(exp)

print("/nОбщее количество найденных стажей работы:", num_experience)
