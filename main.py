#  I am going to create a matrix module from scratch which will input number of rows and columns as well as the elements of the matrix.
# I will then perform operations on the matrix

# matrix class in python
class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.columns = m
        self.matrix = self.get_matrix(n, m)

    # function to get the matrix
    def get_matrix(self, n, m):
        # create an empty list
        matrix = []
        # for loop to iterate through the rows
        for i in range(n):
            # temporary list
            temp = list(map(int, input(f"Enter the elements of the row {i+1}: ").split()))
            # throws error if number of elements is greater than or less than the number of columns
            if len(temp) != m:
                raise ValueError("The number of elements in the row is not equal to the number of columns")

            matrix.append(temp)
        # return the matrix
        return matrix
    
def print_matrix(a):
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(a.columns):
            # print the element
            print(a.matrix[i][j], end = " ")
        # print a new line
        print()
    
"""
a = Matrix(2, 2)
1 6
7 4
b = Matrix(2, 2)
5 2
3 8
Addition
c = add(a, b)
5 6
7 8
"""
# function to add two elements
def add_elements(a, b):
    return max(a, b)

# function to multiply two elements
def multiply_elements(a, b):
    return a + b

# function to add two matrices
def add(a, b):
    # check if the dimensions of the matrices are equal
    if a.rows != b.rows or a.columns != b.columns:
        raise ValueError("The dimensions of the matrices are not equal")
    # create an empty matrix
    c = Matrix(a.rows, a.columns)
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(a.columns):
            # add the elements
            c.matrix[i][j] = add_elements(a.matrix[i][j], b.matrix[i][j])
    # return the matrix
    return c

# a = Matrix(2, 2)
# b = Matrix(2, 2)
# c = add(a, b)
# print_matrix(c)

# function to multiply two matrices
def multiply(a, b):
    # check if the number of columns of a is equal to the number of rows of b
    if a.columns != b.rows:
        raise ValueError("The number of columns of a is not equal to the number of rows of b")
    # create an empty matrix
    c = Matrix(a.rows, b.columns)
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(b.columns):
            # for loop to iterate through the columns of a
            for k in range(a.columns):
                # add the elements
                c.matrix[i][j] = add_elements(multiply_elements(a.matrix[i][k], b.matrix[k][j]), c.matrix[i][j])
    # return the matrix
    return c

"""
a = Matrix(2, 2)
1 6
7 4
b = Matrix(2, 2)
5 2
3 8
Multiplication
c = multiply(a, b)
9 14
12 12
"""

a = Matrix(2, 2)
b = Matrix(2, 2)
c = multiply(a, b)
print_matrix(c)