# 1. Даны строки S и S0. Удалить из строки S первую подстроку, совпадающую с S0. 
#Если совпадающих подстрок нет, то вывести строку S без изменений. . 
def remove_substr(S, S0):
    try:
        index = S.index(S0)
        return S[:index] + S[index + len(S0):] 
    except ValueError:
        return S   # если подстрока не найдена, возвращаем исходную строку S без изменений

# Пример использования функции
S = "Hello, World!"
S0 = "Hello,"
print(remove_substr(S, S0))


#2. Дана строка-предложение с избыточными пробелами между словами. 
#Преобразовать ее так, чтобы между словами был ровно один пробел
def fix_spaces(sentence):
    try:
        words = sentence.split()
        fixed_sentence = ' '.join(words)
        return fixed_sentence
    except Exception as e:
        # обработка исключений(выводим сообщение об ошибке и возвращаем исходную строку)
        print(f"Error: {e}")
        return sentence

 # Пример использования функции   
print(fix_spaces("Это    предложение    содержит    лишние пробелы     "))
