#Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE. 

import random


def matrix_creative(rows,columns):
   return[[random.randint(-100, 100) for _ in range(rows)]for _ in range(columns)]


def matrix_have_positive_elements(matrix):
   return any(any(elem > 0 for elem in row) for row in matrix)


matrix = matrix_creative(3,3)
print(matrix_have_positive_elements(matrix))
