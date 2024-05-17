class Person:
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count=Person.count+1
    
    @staticmethod
    def total_people():
        return f"Количество людей: {Person.count}"

print(Person.total_people())        
p = Person("Jhon")
print(Person.total_people())
p1 = Person("Dan")
print(Person.total_people())1
