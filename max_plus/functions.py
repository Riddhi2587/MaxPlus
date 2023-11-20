#  I am going to create a matrix module from scratch which will input number of rows and columns as well as the elements of the matrix.
# I will then perform operations on the matrix

# E = float('-inf')

from multimethod import multimethod 

# matrix class in python
class Matrix:
    def __init__(self, string, zeros = False, rows = 0, columns = 0):   
        if zeros == True:
            self.rows = rows
            self.columns = columns
            self.matrix = [[float(0) for i in range(columns)] for j in range(rows)]
            return
        
        else:
            # remove the first and last character
            string = string[1:-1]
            # print(string)
            # split the string by comma
            string = string.split(",")
            # print(string)
            # create an empty matrix as a variable of the class
            self.matrix = []
            # create empty list
            # rows = []
            # print(len(string))
            # define private varialbes for number of rows and columns and find them
            self.rows = len(string)
            self.columns = len(string[0].split(" "))
            for row in string:
                # remove leading spaces
                row = row.lstrip()
                # remove the first and last character
                row = row[1:-1]
                # # split the string by space
                row = row.split(" ")
                # print(len(row))
                # print(row)
                # # convert the string to a float
                row = [float(i) for i in row]
                # print(row)
                # # append the row to the matrix
                self.matrix.append(row)
        # print(self.matrix) 
    
    # def print_matrix(self):
    #     # for loop to iterate through the rows
    #     for i in range(self.__rows):
    #         # for loop to iterate through the columns
    #         for j in range(self.__columns):
    #             # print the element
    #             print(self.matrix[i][j], end = " ")
    #         # print a new line
    #         print()
    
     
    
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
2 
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
    return round(max(a, b), 6)

# function to multiply two elements
def multiply_elements(a, b):
    # if a == e or b == e:
    #     return e
    return round(a + b, 6)

# function to add two matrices
def add(a: Matrix, b: Matrix):
    # check if the dimensions of the matrices are equal
    if a.rows != b.rows or a.columns != b.columns:
        raise ValueError("The dimensions of the matrices are not equal")
    # create an empty matrix
    c = Matrix("", True, a.rows, a.columns)
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(a.columns):
            # add the elements
            c.matrix[i][j] = add_elements(a.matrix[i][j], b.matrix[i][j])
    return c

# a = Matrix(2, 2)
# b = Matrix(2, 2)
# c = add(a, b)
# print_matrix(c)

# function to multiply two matrices
@multimethod
def multiply(a: Matrix, b: Matrix):
    # check if the number of columns of a is equal to the number of rows of b
    if a.columns != b.rows:
        raise ValueError("The number of columns of a is not equal to the number of rows of b")
    # create an empty matrix
    c = Matrix("", True, a.rows, b.columns)
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(b.columns):
            # for loop to iterate through the columns of a
            for k in range(a.columns):
                c.matrix[i][j] = add_elements(multiply_elements(a.matrix[i][k], b.matrix[k][j]), c.matrix[i][j])
    return c

@multimethod
def multiply(a: int, b: Matrix):
    # create an empty matrix
    c = Matrix("", True, b.rows, b.columns)
    # for loop to iterate through the rows
    for i in range(b.rows):
        # for loop to iterate through the columns
        for j in range(b.columns):
            c.matrix[i][j] = multiply_elements(a, b.matrix[i][j])
    return c

def subtract(a: Matrix, b: float):
    # create an empty matrix
    c = Matrix("", True, a.rows, a.columns)
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(a.columns):
            c.matrix[i][j] = a.matrix[i][j] - b
    return c

# write a function to find the power of a matrix
def power(a, n):
    # check if the matrix is square
    if a.rows != a.columns:
        raise ValueError("The matrix is not square")
    # create a new matrix
    # c = Matrix("", True, a.rows, a.columns)
    c = a
    # # initialize c as identity matrix
    # for i in range(a.rows):
    #     for j in range(a.columns):
    #         if i == j:
    #             c.matrix[i][j] = 1
    #         else:
    #             c.matrix[i][j] = 0
    # multiply the matrix n times
    for i in range(n-1):
        c = multiply(c, a)
    return c

def fact(n):
    return n*(n+1)/2

def maxEl(a: Matrix):
    maxi = float('-inf')
    for i in range(a.rows):
        for j in range(a.columns):
            if a.matrix[i][j] > maxi:
                maxi = a.matrix[i][j]
    return maxi

def exp(a: Matrix):
    ans = subtract(a, 1)
    tempMat = a
    t = maxEl(a)
    # check if t is float or int
    if t.is_integer():
        t = int(t)
    else:
        t = int(t) + 1

    # print(t)

    for i in range(t-1):
        tempMat = multiply(tempMat, a)
        divi = fact(i+2)
        # print(divi)
        ans = add(ans, subtract(tempMat, divi))

    return ans

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

a = Matrix("[[1.5 1.9 1.5], [2 1.4 1.5], [1.4 1.6 1.9]]")
# a = Matrix("[[1 2 3], []]")
# print(a.rows)
# b = Matrix("[[5 2], [3 8]]")
# b = Matrix(2, 2)
# c = multiply(2, a)
# c = power(a, 6)

c = exp(a)
# c = b
print_matrix(c)

"""
Doubts
- round
- eigenvalue, eigenvector
"""
