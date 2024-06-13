#В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

def matrix_sum_and_multiply(matrix, N):
   matrix_sum = sum(matrix[N-1])
   matrix_multiply = 1
   for elem in matrix[N-1]:
       matrix_multiply*=elem
   print(f'Сумма элементов строки {N}:{matrix_sum}')
   print(f'Произведение элементов строки {N}:{matrix_multiply}')

matrix_sum_and_multiply(matrix,1)
