#Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
#Добавьте методы для сложения, вычитания и умножения матриц.
import pickle

class Matrix:
    columns = 0
    rows = 0


    def __init__(self, col, row, matrix):
        self.columns = col
        self.rows = row
        self.matrix = matrix
            
    def addiction(self, other):
        if self.rows !=other.rows or self.columns != other.columns:
            raise ValueError(f"Нельзя сложить матрицу {self.matrix} c {other.matrix}")   
        
        result_matrix = []

        for i in range(self.rows):
            new_row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)]
            result_matrix.append(new_row)
        return Matrix(self.columns, self.rows, result_matrix)
    
    def subtraction(self, other):
        if self.rows !=other.rows or self.columns != other.columns:
            raise ValueError(f"Нельзя вычесть матрицу {self.matrix} c {other.matrix}")     
        
        result_matrix = []

        for i in range(self.rows):
            new_row = [self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)]
            result_matrix.append(new_row)
        return Matrix(self.columns, self.rows, result_matrix)
    
    def multypli(self,other):
        if(self.columns!=other.rows):
            raise ValueError(f"Нельзя перемножить матрицу {self.matrix} c {other.matrix}")     
        result_matrix = []

        for i in range(self.rows):
            new_row = []
            for j in range(other.columns):
                new_row.append(sum(self.matrix[i][k] + other.matrix[k][j] for j in range(self.columns) for k in range(self.columns)))
            result_matrix.append(new_row)
        return Matrix(self.columns, self.rows, result_matrix)
        

    def show(self):
        matrix_str = " "
        for  row in self.matrix:
            matrix_str += " ".join(str(elem) for elem in row) + "\t"
        print(f"\nMatrix: {matrix_str}")
        

m1 = Matrix(2,2,[[1,2],[2,2]])
m2 = Matrix(2,2,[[2,2],[1,2]])

m3 = m1.addiction(m2)
m4 = m1.subtraction(m2)
m5 = m1.multypli(m2)

m3.show()
m4.show()
m5.show()


def save_def(obj, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)

def load_def(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

save_def(m1, 'matrix1.pkl')
save_def(m2, 'matrix2.pkl')
save_def(m3, 'result_matrix.pkl')


loaded_m1 = load_def('matrix1.pkl')
loaded_m2 = load_def('matrix2.pkl')
loaded_result = load_def('result_matrix.pkl')
