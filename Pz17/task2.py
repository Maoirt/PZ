
# Дни недели пронумерованы следующим образом: 1 — понедельник,
# 2 — вторник, ..., 6 — суббота, 7 — воскресенье. Дано целое число K, лежащее в диапазоне
# 1-365. Определить номер дня недели для K-го дня года, если известно, что в этом году 1
# января было субботой.


import tkinter as tk

def calculate_weekday():
    k = int(entry.get())
    weekday = (k + 5) % 7
    result_label.config(text="Номер дня недели: " + str(weekday if weekday != 0 else 7))

root = tk.Tk()
root.title("Определение дня недели")

input_label = tk.Label(root, text="Введите номер дня в году (от 1 до 365):")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Определить день недели", command=calculate_weekday)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()