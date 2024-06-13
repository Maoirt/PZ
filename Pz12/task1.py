#В последовательности на n целых чисел умножить все элементы на первый максимальный элемент.

def multiply_by_max(seq):
   if not seq:
       return []
   max_element = max(seq)
   return[elem*max_element for elem in seq]
  
sequence = [1,2,3,4,5]
result_sequence = multiply_by_max(sequence)
print(result_sequence)
