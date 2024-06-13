#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Количество элементов первого и второго файлов:
#Элементы последней трети:
#Индекс максимального элемента последней трети

import random

#Генерация последовательности случайных чисел для первого файла

with open('file1.txt', 'w') as file1:
  sequence1 = [random.randint(-100,100) for _ in range(20)]
  file1.write(' '.join(map(str,sequence1)))

#Генерация последовательности случайных чисел для второгоф файла
with open('file2.txt', 'w') as file2:
  sequence2 = [random.randint(-100,100) for _ in range(20)]
  file2.write(' '.join(map(str,sequence2)))

with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('output', 'w') as output_file:
  data1 = list(map(int, file1.read().split()))
  data2 = list(map(int, file2.read().split()))

  total_elements = len(data)+len(data2)
  last_third_elements = data1[-len(data1)//3:] + data2[-len(data2)//3:]

  max_elements_index = last_third_elements.index(max(last_third_elements))

  output_file.write(f'Элементы первого файла: {data1}\n')
  output_file.write(f'Элементы второго файла: {data2}\n')
  output_file.write(f'Элементы последней трети: {last_third_elements}\n')
  output_file.write(f'Индекс максимального элемента последней трети: {max_elements_index}\n')
