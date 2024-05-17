# Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой 
# организации. БД должна содержать таблицу Торговая точка со следующей структурой 
# записи: этаж, площадь, наличие кондиционера и стоимость аренды в день

import sqlite3

conn = sqlite3.connect('trading_point.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Trading_Point
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                floor INTEGER,
                square REAL,
                conditioner TEXT,
                cost_arend REAL)''')

conn.commit()

def add_shop_point(floor, square, conditioner, cost_arend):
    cursor.execute('''INSERT INTO Trading_Point (floor, square, conditioner, cost_arend)
                      VALUES (?, ?, ?, ?)''', (floor, square, conditioner, cost_arend))
    conn.commit()

def find_shop_point_by_floor(floor):
    cursor.execute('''SELECT * FROM Trading_Point WHERE floor = ?''', (floor,))  
    return cursor.fetchall()

def find_shop_point_by_con(conditioner):
    cursor.execute('''SELECT * FROM Trading_Point WHERE conditioner = ?''', (conditioner,))
    return cursor.fetchall()

def delete_shop_point_by_id(id):
    cursor.execute('''DELETE FROM Trading_Point WHERE id = ?''', (id,))
    conn.commit()

def update_shop_point_cost(id, new_cost):
    cursor.execute('''UPDATE Trading_Point SET cost_arend = ? WHERE id = ?''', (new_cost, id))
    conn.commit()

add_shop_point(1, 50.5, 'Да', 100.0)
add_shop_point(2, 70.2, 'Нет', 150.0)
add_shop_point(1, 30.0, 'Да', 80.0)

print(find_shop_point_by_floor(1))
print(find_shop_point_by_con('Да'))

delete_shop_point_by_id(2)

update_shop_point_cost(1, 120.0)

conn.close()

# [(1, 1, 50.5, 'Да', 100.0), (3, 1, 30.0, 'Да', 80.0), (4, 1, 50.5, 'Да', 100.0), (6, 1, 30.0, 'Да', 80.0), (7, 1, 50.5, 'Да', 100.0), (9, 1, 30.0, 'Да', 80.0)]
# [(1, 1, 50.5, 'Да', 100.0), (3, 1, 30.0, 'Да', 80.0), (4, 1, 50.5, 'Да', 100.0), (6, 1, 30.0, 'Да', 80.0), (7, 1, 50.5, 'Да', 100.0), (9, 1, 30.0, 'Да', 80.0)]
