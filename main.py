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
    
    def print_matrix(self):
        # for loop to iterate through the rows
        for i in range(self.rows):
            # for loop to iterate through the columns
            for j in range(self.columns):
                # print the element
                print(self.matrix[i][j], end = " ")
            # print a new line
            print()
    
# Object of the above class
# a= Matrix(2, 2)
# b = Matrix(2, 2)
