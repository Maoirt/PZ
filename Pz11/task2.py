# 2. Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно вставив после каждой
# строки строку из символов «*».
  
  
with open('text18-32.txt', 'r', encoding='utf-16') as file:
   read_file = file.read()

with open('text18-32.txt', 'r', encoding='utf-16') as file:
   lines = [file.readline() for _ in range(4)]
  
punctuation_count = sum([1 for char in ''.join(lines) if char in '.,:;!?'])

print(read_file)

print(f'Количество знаков пунктуации в первых четырёх строках: {punctuation_count}')

with open('text18-32.txt', 'r', encoding='utf-16') as file, open('poem.txt', 'w', encoding='utf-8') as poem_file:
   for line in file:
       poem_file.write(line.strip() + '\n****************************\n')
