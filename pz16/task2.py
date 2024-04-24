#Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
#класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
#связанные с социальным положением (например, "семейное положение",
#"количество детей" и т.д.).

class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
class Man(Human):
    def __init__(self, name, age,  status, count_child):
        super().__init__(name,age, "Муж")
        self.status = status
        self.count_child = count_child

    def show(self):
        print(f"\n===\nИмя:{self.name}\nВозраст:{self.age}\nПол:{self.sex}\nСеменойе положение:{self.status}\nКоличество детей: {self.count_child}\n===")


class Woman(Human):
    def __init__(self, name, age, status, count_child):
        super().__init__(name,age,"Женщ")
        self.status = status
        self.count_child = count_child
    def show(self):
        print(f"\n===\nИмя:{self.name}\nВозраст:{self.age}\nПол:{self.sex}\nСеменойе положение:{self.status}\nКоличество детей: {self.count_child}\n===")

man1 = Man("Джон", 37, "Женат", 0)
man1.show()

wom1 = Woman("Соня", 27, "Замужем", "2")
wom1.show()


#Вывод


#===
#Имя:Джон
#Возраст:37
#Пол:Муж
#Семенойе положение:Женат
#Количество детей: 0
#===

#===
#Имя:Соня
#Возраст:27
#Пол:Женщ
#Семенойе положение:Замужем
#Количество детей: 2
#===
