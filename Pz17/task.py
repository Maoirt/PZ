import os
import shutil

# переход в каталог Pz10 и вывод списка файлов
pz11_path = "Pz10"
os.chdir(pz11_path)
print("Список файлов в каталоге Pz10:")
for file in os.listdir():
    if os.path.isfile(file):
        print(file)

# переход в корень проекта, создание папок, перемещение
root_path = os.path.dirname(os.path.abspath(__file__))
test_path = os.path.join(root_path, "test")
test1_path = os.path.join(test_path, "test1")
os.makedirs(test_path, exist_ok=True)
os.makedirs(test1_path, exist_ok=True)

# Перемещение файлов из папок ПЗ6 и ПЗ7
shutil.move(os.path.join("..", "Pz6", "main.py"), test_path)
shutil.move(os.path.join("..", "Pz6", "report.pdf"), test_path)
shutil.move(os.path.join("..", "Pz7", "main.py"), os.path.join(test1_path, "test.txt"))

# Вывод информации о размере файлов в папке test
total_size = 0
for file in os.listdir(test_path):
    file_path = os.path.join(test_path, file)
    total_size += os.path.getsize(file_path)

print(f"Общий размер файлов в папке test: {total_size} байт")

# Найдем файл с самым коротким именем в каталоге PZ11
shortest_filename = min(os.listdir(), key=len)
print(f"Файл с самым коротким именем в каталоге PZ11: {shortest_filename}")

# "Запустим" файл в программе, предположим, что есть программа, которая открывает PDF файлы
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

if pdf_files:
    file_to_open = pdf_files[0]
    os.startfile(file_to_open)  # предполагая, что это откроет файл в программе по умолчанию

# Удалим файл test.txt
os.remove(os.path.join(test1_path, "test.txt"))
