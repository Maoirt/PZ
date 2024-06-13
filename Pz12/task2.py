#2 task. Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string. Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string
input_string = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}'

punctuation_symbols = ''.join(char for char in input_string if char in string.punctuation)
print(punctuation_symbols)
